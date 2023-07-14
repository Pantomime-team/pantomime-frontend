function insertAfter(referenceNode, newNode) {
  referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

window.onload = makeDoubleDelegate(window.onload, () => {
  document.querySelectorAll(".upload-file-input").forEach((upload_input) => {
    const upload_file = upload_input.closest(".upload-file");

    upload_file.addEventListener("click", (e) => {
      upload_input.click();
    });

    upload_input.addEventListener("change", (e) => {
      if (upload_input.files.length) {
        updateThumbnail(upload_file, upload_input, upload_input.files[0]);
      }
    });

    upload_file.addEventListener("dragover", (e) => {
      e.preventDefault();
      upload_file.classList.add("upload-file-over");
    });

    ["dragleave", "dragend"].forEach((type) => {
      upload_file.addEventListener(type, (e) => {
        upload_file.classList.remove("upload-file-over");
      });
    });

    upload_file.addEventListener("drop", (e) => {
      e.preventDefault();

      if (e.dataTransfer.files.length) {
        upload_input.files = e.dataTransfer.files;
        updateThumbnail(upload_file, upload_input, e.dataTransfer.files[0]);
      }

      upload_file.classList.remove("upload-file-over");
    });
  });

  function removeThumbnail(upload_file, upload_input) {
    upload_file.querySelector(".upload-file-thumb").remove();
    upload_file.querySelector(".upload-file-prompt").style.display = "block";
    upload_file.style.display = "flex";

    // Clear files
    upload_input.value = "";
  }

  function updateThumbnail(upload_file, upload_input, file) {
    let thumbnailElement = upload_file.querySelector(".upload-file-thumb");

    if (upload_file.querySelector(".upload-file-prompt")) {
      upload_file.querySelector(".upload-file-prompt").style.display = "none";
    }

    if (!thumbnailElement) {
      thumbnailElement = document.createElement("div");
      thumbnailElement.classList.add("upload-file-thumb");
      upload_file.appendChild(thumbnailElement);
    }

    thumbnailElement.dataset.label = file.name;

    // Show thumbnail for image and video files
    if (file.type.startsWith("image/")) {
      const reader = new FileReader();

      reader.readAsDataURL(file);
      reader.onload = () => {
        thumbnailElement.style.backgroundImage = `url("${reader.result}")`;
      };
    } else if (file.type.startsWith("video/")) {
      const reader = new FileReader();

      // TODO: for god's sake, do not load the whole video
      // X: > beg not to do it
      // X: > do it anyway
      reader.readAsDataURL(file);
      reader.onload = () => {
        let video_container = document.getElementById("thumb-video-preview");

        if (!video_container) {
          video_container = document.createElement("video");
          video_container.id = "thumb-video-preview";
          thumbnailElement.appendChild(video_container);
        }

        video_container.src = reader.result;
        video_container.autoplay = true;
        video_container.loop = true;
        video_container.muted = true;
        video_container.playsinline = true;
      };
    } else {
      thumbnailElement.style.backgroundImage = null;
    }

    let uploadButton = document.getElementById("upload-button");
    if (!uploadButton) {
      const button_div = document.createElement("div");
      const upload_button = document.createElement("button");

      upload_button.innerHTML = "Загрузить видео";
      upload_button.type = "button";
      upload_button.id = "upload-button";

      upload_button.addEventListener("click", (e) => {
        upload_file.style.display = "none";
        upload_button.remove();

        // Create progressbar
        const progressbar = document.createElement("progress");
        progressbar.id = "upload-progressbar";
        progressbar.value = 0;
        progressbar.max = 100;
        insertAfter(upload_file, progressbar);

        // Send file by chunks to /video-upload
        const BYTES_PER_CHUNK = 1024 * 1024; // 1MB chunk sizes.
        const SIZE = file.size;
        let start = 0;
        let end = BYTES_PER_CHUNK;
        let current_chunk = 0;
        let total_chunks = Math.ceil(SIZE / BYTES_PER_CHUNK);
        let finished = false;

        const socket = io({ transports: ["websocket"] });
        socket.connect();

        socket.emit("video-upload", {
          filename: file.name,
          data_chunk: file.slice(start, end),
          current_chunk: current_chunk,
          total_chunks: total_chunks,
        });

        socket.on("on-video-upload-status", (data) => {
          if (!finished && data.status == "finished") {
            let interval = setInterval(() => {
              socket.emit("get-video-process-status");
            }, 1000);

            progressbar.value = 100;
            progressbar.remove();

            // Create please wait message
            const please_wait = document.createElement("p");
            please_wait.innerHTML = "Пожалуйста, подождите...";
            insertAfter(upload_file, please_wait);

            socket.on("get-video-process-status", (data) => {
              if (data.status == "finished") {
                let output_file = new Blob([data.return_value], {
                  type: "text/plain",
                });

                let download_link = document.createElement("a");
                download_link.href = URL.createObjectURL(output_file);
                download_link.download = "translated_video.txt";
                download_link.click();

                // Reset all to how it was before
                removeThumbnail(upload_file, upload_input);
                clearInterval(interval);
                please_wait.remove();
                socket.disconnect();
              }
            });

            finished = true;
          }

          if (!finished && data.return_value != null) {
            current_chunk = data.return_value;
            start = BYTES_PER_CHUNK * current_chunk;
            end = start + BYTES_PER_CHUNK;

            progressbar.value = Math.round(
              (current_chunk / total_chunks) * 100
            );

            socket.emit("video-upload", {
              filename: file.name,
              data_chunk: file.slice(start, end),
              current_chunk: current_chunk,
              total_chunks: total_chunks,
            });
          }
        });

        // upload_button.removeEventListener("click");
      });

      button_div.appendChild(upload_button);
      insertAfter(upload_file, button_div);
    }
  }
});
