window.onload = makeDoubleDelegate(window.onload, () => {
  let webcam_stream = document.getElementById("webcam-stream");
  let webcam_canvas = document.getElementById("webcam-stream-canvas");
  let webcam_canvas_ctx = webcam_canvas.getContext("2d");

  let webcam_enable_btn = document.getElementById("webcam-stream-icon");
  webcam_enable_btn.addEventListener("click", () => {
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
        }, 1000 / 30); // 30 FPS
      })
      .catch((err) => {
        console.log("[Error] " + err);
      });

    webcam_enable_btn.style.display = "none";

    // Remove the event listener
    webcam_enable_btn.removeEventListener("click", () => {});
  });
});
