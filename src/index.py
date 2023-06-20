import json
import streamlit as st
import requests

# from streamlit_webrtc import webrtc_streamer, VideoHTMLAttributes

# # https://medium.com/mlearning-ai/live-webcam-with-streamlit-f32bf68945a4

# st.title("Webcam Test")
# st.subheader("This is a test of the webcam")
# st.write("This is a test of the webcam")

# # Get the data from the user's webcam
# webrtc_streamer(
#     key="example",
#     video_html_attrs=VideoHTMLAttributes(
#         autoPlay=True, controls=False, style={"width": "100%"}
#     ),
# )

predict_route = "http://localhost:80/predict"  # Temporarily

def predict(file):
    x = requests.post(predict_route, files={"file": file.getvalue()})
    return x.text

def predict_from_path(path):
    with open(path, "rb") as f:
        x = requests.post(predict_route, files={"file": f})
        x.content.decode("utf-8")
        return x.text

with st.container():
    st.title("ASL Translator")
    st.subheader("Translate sign language to russian")

    holder = st.empty()

    file = holder.file_uploader(
        "Upload a video to translate from ASL",
        type=['.mp4'],
        accept_multiple_files=False
        )

    if file is not None:
        # Hide the holder
        holder.empty()
        holder.write("Processing video. Please, wait...")
        
        # Send file to backend and decode the result from the json
        result = json.loads(predict(file))
        st.write(result)

        holder.empty()

        st.balloons()

# pip remove 