import json
import streamlit as st
import requests
from annotated_text import annotated_text

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


#Cute wave
page_bcg_1 = """ 
<style>
[data-testid="stAppViewContainer"] {
background-color: #000218;
opacity: 1;
background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #000218 40px ), repeating-linear-gradient( #35335855, #353358 );
  }

<style>
"""

#dots diagonally
page_bcg = """ 
<style>
[data-testid="stAppViewContainer"] {
background-color: #000218;
opacity: 1;
background-image:  radial-gradient(#353358 2px, transparent 2px), radial-gradient(#353358 2px, #000218 2px);
background-size: 80px 80px;
background-position: 0 0,40px 40px;
  }

<style>
"""

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


#Change bcg color
#st.markdown(page_bcg_1, unsafe_allow_html=True)

predict_route = "http://localhost:80/predict"  # Temporarily

def predict(file):
    x = requests.post(predict_route, files={"file": file.getvalue()})
    return x.text

def predict_from_path(path):
    with open(path, "rb") as f:
        x = requests.post(predict_route, files={"file": f})
        x.content.decode("utf-8")
        return x.text

st.markdown("<h1 style='text-align: center; color: white;'>Pantomime</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image("https://w-dog.ru/wallpapers/5/18/289291145046987/evropejskaya-koshka-dikij-kot-morda-vzglyad.jpg", width=300, use_column_width=True, caption="logo trust me bro")

with col2:
    #st.title("Pantomime")
    st.write(" is Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id ")


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


st.markdown("<h1 style='text-align: center; color: white;'>Our beloved Team</h1>", unsafe_allow_html=True)


# Vladislav Kulikov
image = "https://w-dog.ru/wallpapers/5/18/289291145046987/evropejskaya-koshka-dikij-kot-morda-vzglyad.jpg"
col1, col2 = st.columns([3,2])

with col1:
    st.title("Vladislav Kulikov")

    annotated_text(
        ("Team Lead", "", "#353358"),
        " ",
        ("ML-Team", "", "#ff5436"),
        )

with col2:
    st.image(image, width=300, caption="cutie kitty", use_column_width=True)

# Daniel Satakhrushev
image = "https://w-dog.ru/wallpapers/5/18/289291145046987/evropejskaya-koshka-dikij-kot-morda-vzglyad.jpg"
col1, col2 = st.columns([3,2])

with col1:
    st.title("Daniel Satakhrushev")

    annotated_text(
        ("Frontend developer", "", "#8eaf20"),
        " ",
        ("ML-Team", "", "#ff5436"),
        )
    

with col2:
    st.image(image, width=300, caption="cutie kitty", use_column_width=True)

# Ivan Chernakov
image = "https://w-dog.ru/wallpapers/5/18/289291145046987/evropejskaya-koshka-dikij-kot-morda-vzglyad.jpg"

col1, col2 = st.columns([3,2])

with col1:
    st.title("Ivan Chernakov")

    annotated_text(
        ("Lead Designer", "", "#6200ee"),
        " ",
        ("Frontend developer", "", "#8eaf20"),
        " ",
        ("ML-Team", "", "#ff5436"),
        )

with col2:
    st.image(image, width=300, caption="cutie kitty", use_column_width=True)

# Alexandr Kudasov
image = "https://w-dog.ru/wallpapers/5/18/289291145046987/evropejskaya-koshka-dikij-kot-morda-vzglyad.jpg"

col1, col2 = st.columns([3,2])

with col1:
    st.title("Alexandr Kudasov")

    annotated_text(
        ("Backend developer", "", "#e39801"),
        " ",
        ("ML-Team", "", "#ff5436"),
        )

with col2:
    st.image(image, width=300, caption="cutie kitty", use_column_width=True)

# Vitaliy Alifanov
image = "https://w-dog.ru/wallpapers/5/18/289291145046987/evropejskaya-koshka-dikij-kot-morda-vzglyad.jpg"

col1, col2 = st.columns([3,2])

with col1:
    st.title("Vitaliy Alifanov")

    annotated_text(
        ("ML-Team", "", "#ff5436"),
        )

with col2:
    st.image(image, width=300, caption="cutie kitty", use_column_width=True)

# Daria Verevkina
image = "https://w-dog.ru/wallpapers/5/18/289291145046987/evropejskaya-koshka-dikij-kot-morda-vzglyad.jpg"

col1, col2 = st.columns([3,2])

with col1:
    st.title("Daria Verevkina")

    annotated_text(
        ("Designer", "", "#6200ee"),
        )
    
with col2:
    st.image(image, width=300, caption="cutie kitty", use_column_width=True)

# Nastya Palashkina
image = "https://w-dog.ru/wallpapers/5/18/289291145046987/evropejskaya-koshka-dikij-kot-morda-vzglyad.jpg"

col1, col2 = st.columns([3,2])

with col1:
    st.title("Nastya Palashkina")

    annotated_text(
        ("Designer", "", "#6200ee"),
        )
    
with col2:
    st.image(image, width=300, caption="cutie kitty", use_column_width=True)

