from function_generate_images import generate_image
from function_images_to_video import generate_video
import function_generate_images 
import function_images_to_video

#Variablen aus den anderen Files sollen hier noch hinzugefügt werden, damit die hier im main.py geändert werden können (z.B. wie viele Bilder generiert werden usw.)
function_generate_images.steps = 1
function_images_to_video.fps = 1


def main(user_prompt):
    generate_image(user_prompt)
    generate_video()

main("house")