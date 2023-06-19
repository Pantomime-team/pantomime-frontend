import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoHTMLAttributes

# https://medium.com/mlearning-ai/live-webcam-with-streamlit-f32bf68945a4

st.title("Webcam Test")
st.subheader("This is a test of the webcam")
st.write("This is a test of the webcam")

# Get the data from the user's webcam
webrtc_streamer(
    key="example",
    video_html_attrs=VideoHTMLAttributes(
        autoPlay=True, controls=False, style={"width": "100%"}
    ),
)

st.balloons();
