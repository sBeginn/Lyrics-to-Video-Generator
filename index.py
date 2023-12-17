import streamlit as st
import os

current_path = os.path.dirname(__file__)

def start():
    st.title("Lyrics-to-Video-Generator")

    user_input_songname = st.text_input("Songname")
    user_input_artist = st.text_input("Artist")

    button_generate = st.button("Generate")
    
    if button_generate:
        show_generated_video()

def show_generated_video():
    video_path = current_path + "/generated_video/output_video.mp4"

    # Öffnen Sie die Datei im Binärmodus und lesen Sie die Daten
    with open(video_path, "rb") as f:
        video_bytes = f.read()

    # Zeigen Sie das Video mit st.video an
    st.video(video_bytes, format="video/mp4")

start()
