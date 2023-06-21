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

# Background Color For Columns
column_bcg = """
    <style>
    div[data-testid="stHorizontalBlock"] > div:First-of-type {
    display: flex;
    -webkit-box-align: top;
    align-items: top;
    -webkit-box-pack: top;
    padding: 1rem;
    background-opacity: 0.5;
    background-color: rgb(35, 33, 58);
    border-radius: 0.5rem;
    }
    div[data-testid="stHorizontalBlock"] > div:Last-of-type {
    display: flex;
    -webkit-box-align: center;
    align-items: top;
    -webkit-box-pack: center;
    padding: 1rem;
    background-opacity: 0.5;
    background-color: rgb(35, 35, 58);
    border-radius: 0.5rem;
    }
    </style>
    """
st.markdown(column_bcg, unsafe_allow_html=True)

# To Round Images
rounding_images = """
    <style>
    img {
    border-radius: 0.5rem;
    }
    </style>
    """
st.markdown(rounding_images, unsafe_allow_html=True)

# Cute Wave Background
page_bcg = """ 
<style>
[data-testid="stAppViewContainer"] {
background-color: #353358;
opacity: 1;
background-image: radial-gradient(circle at center center, #000218, #353358), repeating-radial-gradient(circle at center center, #000218, #000500, 40px, transparent 80px, transparent 120px);
background-blend-mode: multiply;
}
<style>
"""
st.markdown(page_bcg, unsafe_allow_html=True)

# Hide Streamlit Additionals
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

file_uploader_bcg = """
        <style>
        div[data-testid="stFileUploader"] > div:Fist-of-type {
        background-color: #353358;
        background: #353358;
        opacity: 1;
        border-radius: 0.5rem;
        }
        </style>
        """
st.markdown(file_uploader_bcg, unsafe_allow_html=True)




predict_route = "http://localhost:80/predict"  # Temporarily

def predict(file):
    x = requests.post(predict_route, files={"file": file.getvalue()})
    return x.text

def predict_from_path(path):
    with open(path, "rb") as f:
        x = requests.post(predict_route, files={"file": f})
        x.content.decode("utf-8")
        return x.text

# Title
st.markdown("<h1 style='text-align: center; color: white;'>Pantomime</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("https://w-dog.ru/wallpapers/5/18/289291145046987/evropejskaya-koshka-dikij-kot-morda-vzglyad.jpg", width=300, use_column_width=False, caption="logo trust me bro")
    #st.image("https://avatars.githubusercontent.com/u/136185091?s=200&v=4", width=250, use_column_width=True, caption="logo trust me bro")

with col2:
    #st.title("Pantomime")
    st.write(" is Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore m dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id ")


with st.container():
    st.markdown("<h1 style='text-align: center; color: white;'>RSL Translator</h1>", unsafe_allow_html=True)
    
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
col2, col1 = st.columns([2,3])

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
        ("Frontend developer", "", "#8eaf20"),
        " ",
        ("Lead Designer", "", "#6200ee"),
        " ",
        
        ("ML-Team", "", "#ff5436"),
        )

with col2:
    st.image(image, width=300, caption="cutie kitty", use_column_width=True)


# Alexandr Kudasov
image = "https://w-dog.ru/wallpapers/5/18/289291145046987/evropejskaya-koshka-dikij-kot-morda-vzglyad.jpg"

col2, col1 = st.columns([2,3])

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

col2, col1 = st.columns([2,3])

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


# Links 
st.markdown("<h1 style='text-align: center; color: white;'>Links</h1>", unsafe_allow_html=True)
# Button to Github with link
import webbrowser

url_github = 'https://github.com/Pantomime-team'
url_capstone = 'https://capstone.innopolis.university/docs/groups/pantomime/'

col1, col2 = st.columns([1,3.5])
with col1:
    if st.button('Our GitHub'):
        webbrowser.open_new_tab(url_github)

with col2:
    if st.button('Our project Timeline'):
        webbrowser.open_new_tab(url_capstone)


