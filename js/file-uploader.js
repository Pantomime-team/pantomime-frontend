window.onload = makeDoubleDelegate(window.onload, () => {
  document.querySelectorAll(".upload-file-input").forEach((inputElement) => {
    const upload_file = inputElement.closest(".upload-file");

    upload_file.addEventListener("click", (e) => {
      inputElement.click();
    });

    inputElement.addEventListener("change", (e) => {
      if (inputElement.files.length) {
        updateThumbnail(upload_file, inputElement.files[0]);
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
        inputElement.files = e.dataTransfer.files;
        updateThumbnail(upload_file, e.dataTransfer.files[0]);
      }

      upload_file.classList.remove("upload-file-over");
    });
  });

  function updateThumbnail(upload_file, file) {
    let thumbnailElement = upload_file.querySelector(".upload-file-thumb");

    if (upload_file.querySelector(".upload-file-prompt")) {
      upload_file.querySelector(".upload-file-prompt").remove();
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
        thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
      };
    } else if (file.type.startsWith("video/")) {
      const reader = new FileReader();

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
  }
});
