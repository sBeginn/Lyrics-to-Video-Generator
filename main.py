from function_generate_images import generate_image
from function_generate_images import samples
from function_generate_images import steps
from function_images_to_video import generate_video
from function_images_to_video import fps
from function_read_lyrics import read_lyrics
from function_read_lyrics import spacy_words
from function_transitions import transitions
from function_warp_affine import generate_rotated_images
from function_warp_affine import song_duration
from function_audio_connection import download_audio
from function_audio_connection import audio_with_video_conncetion
import function_generate_images 
import function_images_to_video
import function_read_lyrics
import function_transitions
import function_audio_connection
import function_warp_affine
import os

current_path = os.path.dirname(__file__)
folder_generated_images = current_path + "/generated_images"
folder_generated_video = current_path + "/generated_video"

if not os.path.exists(folder_generated_images):
    os.makedirs(folder_generated_images)
    
if not os.path.exists(folder_generated_video):
    os.makedirs(folder_generated_video)


def main():
    input_songname = input("Songname:")
    input_artist = input("Artist:")
    input_url = input("url:")
    samples_warp = song_duration(input_songname, input_artist)
    
    read_lyrics(input_songname, input_artist)
    spacy_words(input_songname, input_artist)
    generate_image(input_songname, input_artist)
    generate_rotated_images(samples_warp)
    generate_video()
    download_audio(input_url)
    audio_with_video_conncetion()

main()



