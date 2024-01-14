from diffusers import AutoPipelineForText2Image
import torch
from matplotlib import pyplot as plt
import os
import random


current_path = os.path.dirname(__file__)

pretrained_model = "runwayml/stable-diffusion-v1-5"

steps = 20
samples = 1

def generate_image(input_songname, input_artist):

    # Pfad für die generierten Bilder
    output_folder = current_path + "/generated_images/"
    
    # Pfad zur Textdatei mit den zusammengefassten Songtexten
    text_files = [
        current_path + f"/lyrics_{input_songname}_{input_artist}_part1.txt",
        current_path + f"/lyrics_{input_songname}_{input_artist}_part2.txt",
        current_path + f"/lyrics_{input_songname}_{input_artist}_part3.txt"
    ]
    
    
    for text_file in text_files:
        pipeline = AutoPipelineForText2Image.from_pretrained(
            pretrained_model, 
            torch_dtype=torch.float16, 
            safety_checker=None, 
            requires_safety_checker=False
        ).to("cuda")

        with open(text_file, "r", encoding="utf-8") as file:
            prompt = file.read()

        for sample in range(samples):
            # Generiere den Dateinamen für das Bild
            random_name = random.randint(1000, 9999)  
            image_path = output_folder + f"output_{random_name}.png"

            # Generiere das Bild
            generated_image = pipeline(prompt, num_inference_steps=steps).images[0]

            # Speichere das Bild
            generated_image.save(image_path)
            

            

