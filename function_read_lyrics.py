from lyricsgenius import Genius
import os
import re
from transformers import pipeline

token = "SJT0EPoDLSVfMvvdwbQ41GTyplVGUIjG_N8UxVSCpNtyY6mbtSEq4FrwfxEKwRuD"
genius = Genius(token)

current_path = os.path.dirname(__file__)

def remove_bracketed_text(text):
    # Entfernt alles zwischen eckigen Klammern, einschließlich der Klammern selbst
    return re.sub(r'\[.*?\]', '', text)

def read_lyrics(input_songname, input_artist):

    song = genius.search_song(input_songname, input_artist)

    file_lyrics = current_path + f"//lyrics_{input_songname}_{input_artist}.txt"

    if song:

        original_lyrics = song.lyrics
        
        filtered_lyrics = remove_bracketed_text(original_lyrics)

        filtered_lyrics = '\n'.join(filtered_lyrics.splitlines()[1:])

        myfile = open(file_lyrics, "w", encoding="utf-8")
        myfile.write(filtered_lyrics)
        myfile.close()
    else:
        print("Not found")

def text_summarizer(input_songname, input_artist):

    summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")

    file_lyrics = current_path + f"//lyrics_{input_songname}_{input_artist}.txt"

    with open(file_lyrics, "r", encoding="utf-8") as file:
        text = file.read()

    summary_text = summarizer(text, max_length=100, min_length=5, do_sample=False)[0]['summary_text']

    summary_file = current_path + f"//lyrics_{input_songname}_{input_artist}.txt"

    with open(summary_file, "w", encoding="utf-8") as file:
        file.write(summary_text)
