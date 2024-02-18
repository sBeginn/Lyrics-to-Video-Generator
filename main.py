from function_generate_images import generate_image
from function_images_to_video import generate_video
from function_read_lyrics import read_lyrics
from function_read_lyrics import spacy_words
from function_warp_affine import generate_rotated_images
from function_warp_affine import song_duration
from function_audio_connection import download_audio
from function_audio_connection import audio_with_video_connection
import os

# Path to current file
current_path = os.path.dirname(__file__)

# Paths to the images & video folder
folder_generated_images = current_path + "/generated_images"
folder_generated_video = current_path + "/generated_video"

# Check if folder for images & video exists
if not os.path.exists(folder_generated_images):
    os.makedirs(folder_generated_images)
    
if not os.path.exists(folder_generated_video):
    os.makedirs(folder_generated_video)

# Main function for create a dynamic music video from the lyrics
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
    audio_with_video_connection()

main()



