import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import os
from lyricsgenius import Genius
import re
import random

# Token for connection with genius (enter your own token)
token = "SJT0EPoDLSVfMvvdwbQ41GTyplVGUIjG_N8UxVSCpNtyY6mbtSEq4FrwfxEKwRuD"
genius = Genius(token)

# Path to current file
current_path = os.path.dirname(__file__)

# Function to remove special character from the lyric
def remove_bracketed_text(text):
    return re.sub(r'\[.*?\]', '', text)

# Function to read the song lyrics
def read_lyrics(input_songname, input_artist):

    # Use the genius library to find the song
    song = genius.search_song(input_songname, input_artist)

    # Path and textfile for song lyric
    file_lyrics = current_path + f"//lyrics_{input_songname}_{input_artist}.txt"
    
    # Check if song lyric exists
    if song:

        # Find song lyric
        original_lyrics = song.lyrics
        
        # Optimized the song lyrics (remove everything that is not important)
        filtered_lyrics = remove_bracketed_text(original_lyrics)

        # Remove the first line in the lyric -> (not important infos)
        filtered_lyrics = '\n'.join(filtered_lyrics.splitlines()[1:])

        # Save the lyric in the text file 
        myfile = open(file_lyrics, "w", encoding="utf-8")
        myfile.write(filtered_lyrics)
        myfile.close()
            
    else:
        print("Not found")

# Function to filter the important words from the lyric
def spacy_words(input_songname, input_artist):
    
    # Language dictionary
    nlp = spacy.load("en_core_web_sm")
    
    #Path and textfile for song lyric
    file_lyrics = current_path + f"//lyrics_{input_songname}_{input_artist}.txt"
    
    # Open and read textfile
    with open(file_lyrics, "r", encoding="utf-8") as file:
        lyrics = file.read()
        
    # Split the text into three parts
    total_length = len(lyrics)
    part_length = total_length // 3

    part1 = lyrics[:part_length]
    part2 = lyrics[part_length:2 * part_length]
    part3 = lyrics[2 * part_length:]
    
    # Processed the parts
    for i, part in enumerate([part1, part2, part3]):
        
        # NLP process for actual part 
        about_doc = nlp(part)
        
        # Create set for the nouns -> set because we dont want duplicates
        unique_nouns = set()
        #unique_adjectives = set()
        
        # Loop to filter all "Nouns" in the part
        for token in about_doc:
            # .lemma is a function to reduce a word to the basic form (we dont want the same words only in different time forms in the textfile)
            if token.pos_ == "NOUN" and token.lemma_ in nlp.vocab:
                # All words are lower case
                noun_lemma = token.lemma_.lower()
                
                # Add "Nouns" to the set
                unique_nouns.add(noun_lemma)

            #if token.pos_ == "ADJ" and token.lemma_ in nlp.vocab:
                #adj_lemma = token.lemma_.lower()
                #unique_adjectives.add(adj_lemma)
        
        # Select random nouns for the textfile -> important to generate the image (actual 2 words but if you want you can change)
        selected_nouns = random.sample(list(unique_nouns), min(2, len(unique_nouns)))
        #selected_adjectives = random.sample(list(unique_adjectives), min(1, len(unique_adjectives)))
       
        # Create textfile for every part and enter 2 random nouns       
        summary_file = current_path + f"//lyrics_{input_songname}_{input_artist}_part{i+1}.txt"
        with open(summary_file, "w", encoding="utf-8") as file:
            file.write(", ".join(selected_nouns) + ", ")
            #file.write(", ".join(selected_adjectives))        
    




