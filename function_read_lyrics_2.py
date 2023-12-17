import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import os
from lyricsgenius import Genius
import re


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


def spacy_words(input_songname, input_artist):
    nlp = spacy.load("en_core_web_sm")

    file_lyrics = current_path + f"//lyrics_{input_songname}_{input_artist}.txt"
    
    with open(file_lyrics, "r", encoding="utf-8") as file:
        lyrics = file.read()
        
    # Split the text into three parts
    total_length = len(lyrics)
    part_length = total_length // 3

    part1 = lyrics[:part_length]
    part2 = lyrics[part_length:2 * part_length]
    part3 = lyrics[2 * part_length:]
    
    
    for i, part in enumerate([part1, part2, part3]):
        
        about_doc = nlp(part)
        
        unique_nouns = set()
        unique_adjectives = set()
        
        for token in about_doc:
            if token.pos_ == "NOUN" and token.lemma_ in nlp.vocab:
                noun_lemma = token.lemma_.lower()
                unique_nouns.add(noun_lemma)

            if token.pos_ == "ADJ" and token.lemma_ in nlp.vocab:
                adj_lemma = token.lemma_.lower()
                unique_adjectives.add(adj_lemma)
                
        summary_file = current_path + f"//lyrics_{input_songname}_{input_artist}_part{i+1}.txt"
        with open(summary_file, "w", encoding="utf-8") as file:
            file.write(", ".join(unique_nouns) + ", ")
            file.write(", ".join(unique_adjectives))        
        

        


