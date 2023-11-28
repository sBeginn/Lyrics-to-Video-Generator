from function_generate_images import generate_image
from function_images_to_video import generate_video
from function_read_lyrics import read_lyrics
from function_read_lyrics import text_summarizer
import function_generate_images 
import function_images_to_video
import function_read_lyrics


#Variablen aus den anderen Files sollen hier noch hinzugefügt werden, damit die hier im main.py geändert werden können (z.B. wie viele Bilder generiert werden usw.)
function_generate_images.steps = 20
function_images_to_video.fps = 1
function_generate_images.samples = 1

def main(input_songname, input_artist):
    read_lyrics(input_songname, input_artist)
    text_summarizer(input_songname, input_artist)
    generate_image(input_songname, input_artist)
    generate_video()

main("Godzilla", "Eminem")

