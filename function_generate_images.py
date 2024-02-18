from diffusers import AutoPipelineForText2Image
import torch
from matplotlib import pyplot as plt
import os
import random

# Path to current file
current_path = os.path.dirname(__file__)

# Our pretrained model
pretrained_model = "runwayml/stable-diffusion-v1-5"

# Number of steps (Recommendation: > 25)
steps = 1

# Number of samples (if samples = 1 -> are generate 3 images because of three parts)
samples = 1

# Function to generate images
def generate_image(input_songname, input_artist):

    # Path to the images folder
    output_folder = current_path + "/generated_images/"
    
    # Path to the textfiles
    text_files = [
        current_path + f"/lyrics_{input_songname}_{input_artist}_part1.txt",
        current_path + f"/lyrics_{input_songname}_{input_artist}_part2.txt",
        current_path + f"/lyrics_{input_songname}_{input_artist}_part3.txt"
    ]
    
    # Counts the generated images
    image_counter = 1
    
    # Loop for every textfile
    for text_file in text_files:
        
        # Pretrained model
        pipeline = AutoPipelineForText2Image.from_pretrained(
            pretrained_model, 
            torch_dtype=torch.float16, 
            safety_checker=None, # Safety checker off, because of error messages
            requires_safety_checker=False
               
        ).to("cuda") # Use the GPU 

        # Open the textfile
        with open(text_file, "r", encoding="utf-8") as file:
            # Read the textfile
            prompt = file.read()

        for sample in range(samples):
            # Path and image file
            image_path = output_folder + f"output_{image_counter:03d}.png"
            image_counter += 1

            # Generate the image
            generated_image = pipeline(prompt, num_inference_steps=steps).images[0]

            # Save the image
            generated_image.save(image_path)
            

            

