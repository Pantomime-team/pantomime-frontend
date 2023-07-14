window.onload = makeDoubleDelegate(window.onload, () => {
  let webcam_stream = document.getElementById("webcam-stream");
  let webcam_canvas = document.getElementById("webcam-stream-canvas");
  let webcam_canvas_ctx = webcam_canvas.getContext("2d");
  
  let socket = io({ autoConnect: false });
  let streaming = false;

  let webcam_enable_btn = document.getElementById("webcam-stream-icon");
  webcam_enable_btn.addEventListener("click", () => {
    socket.connect();
    streaming = true;

    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then((stream) => {
        webcam_stream.srcObject = stream;
        webcam_stream.play();

        setInterval(() => {
          webcam_canvas_ctx.drawImage(
            webcam_stream,
            0,
            0,
            webcam_canvas.width,
            webcam_canvas.height
          );

          if (streaming) {
            let image = webcam_canvas.toDataURL("image/jpeg", 1);
            let timestamp = new Date().getTime() / 1000;

            socket.emit("webcam-streaming", {
              image: image,
              timestamp: timestamp,
            });
          }
        }, 1000 / 15); // 15 FPS
      })
      .catch((err) => {
        console.log("[Error] " + err);
      });

    webcam_enable_btn.style.display = "none";

    // Remove the event listener
    webcam_enable_btn.removeEventListener("click", () => {});

    // Add captions callback
    let recognized_text = document.getElementById("recognized-caption");
    socket.on("recognized-caption", (data) => {
      recognized_text.innerHTML += " " + data["gloss"];
      console.log(`${data["gloss"]} took ${data["turnaround_time"]}s`)
    });
  });
});
