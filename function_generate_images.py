from diffusers import AutoPipelineForText2Image
import torch
from matplotlib import pyplot as plt
import os
import random

current_path = os.path.dirname(__file__)

pretrained_model = "runwayml/stable-diffusion-v1-5"

steps = 2
samples = 3


def generate_image(user_prompt):

    value_samples = 0

    while value_samples < samples:
        pipeline = AutoPipelineForText2Image.from_pretrained(
            pretrained_model, 
            torch_dtype=torch.float16, 
            safety_checker=None, 
            requires_safety_checker=False
        ).to("cuda")

        prompt = user_prompt
        random_name = random.randint(1000, 9999)  
        path_images = current_path + f"\\generated_images\\output_{random_name}.png"

        generated_image = pipeline(prompt, num_inference_steps=steps).images[0]

        generated_image.save(path_images)

        value_samples += 1

    #plt.imshow(generated_image)
    #plt.show()
