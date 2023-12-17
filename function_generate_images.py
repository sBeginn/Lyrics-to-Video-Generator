from diffusers import AutoPipelineForText2Image
import torch
from matplotlib import pyplot as plt
import os
import random
from function_read_lyrics import text_summarizer

current_path = os.path.dirname(__file__)

pretrained_model = "runwayml/stable-diffusion-v1-5"

steps = 2
samples = 3

def generate_image(input_songname, input_artist):

    value_samples = 0

    # Pfad für die generierten Bilder
    output_folder = current_path + "/generated_images/"
    
    # Pfad zur Textdatei mit den zusammengefassten Songtexten
    text_file_part_1 = current_path + f"//lyrics_{input_songname}_{input_artist}_part1.txt"
    text_file_part_2 = current_path + f"//lyrics_{input_songname}_{input_artist}_part2.txt"
    text_file_part_3 = current_path + f"//lyrics_{input_songname}_{input_artist}_part3.txt"
    
    
    for part in [text_file_part_1, text_file_part_2, text_file_part_3]:
        while value_samples < samples:
            pipeline = AutoPipelineForText2Image.from_pretrained(
                pretrained_model, 
                torch_dtype=torch.float16, 
                safety_checker=None, 
                requires_safety_checker=False
            ).to("cuda")
            
            with open(part, "r", encoding="utf-8") as file:
                prompt = file.read()

            # Generiere den Dateinamen für das Bild
            random_name = random.randint(1000, 9999)  
            image_path = output_folder + f"output_{random_name}.png"

            # Generiere das Bild
            generated_image = pipeline(prompt, num_inference_steps=steps).images[0]

            # Speichere das Bild
            generated_image.save(image_path)

            value_samples += 1
            

