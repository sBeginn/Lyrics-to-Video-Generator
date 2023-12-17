from function_generate_images import generate_image
from function_images_to_video import generate_video
from function_read_lyrics_2 import read_lyrics
from function_read_lyrics_2 import spacy_words
from function_transitions import transitions
import function_generate_images 
import function_images_to_video
import function_read_lyrics_2
import function_transitions
import os

current_path = os.path.dirname(__file__)
folder_generated_images = current_path + "/generated_images"
folder_generated_video = current_path + "/generated_video"

if not os.path.exists(folder_generated_images):
    os.makedirs(folder_generated_images)
    
if not os.path.exists(folder_generated_video):
    os.makedirs(folder_generated_video)


#Variablen aus den anderen Files sollen hier noch hinzugefügt werden, damit die hier im main.py geändert werden können (z.B. wie viele Bilder generiert werden usw.)
function_generate_images.steps = 50
function_images_to_video.fps = 1
function_generate_images.samples = 3
function_transitions.samples = 10

def main(input_songname, input_artist):
    read_lyrics(input_songname, input_artist)
    spacy_words(input_songname, input_artist)
    generate_image(input_songname, input_artist)
    transitions(function_transitions.samples)
    generate_video()

main("Five Little Ducks", "Raffi")

