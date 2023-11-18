from diffusers import AutoPipelineForText2Image
import torch
from matplotlib import pyplot as plt
import os

current_path = os.path.dirname(__file__)
path_images = current_path + r"\generated_images\output_image.png"


pretrained_model = "runwayml/stable-diffusion-v1-5"

steps = 2


def generate_image(user_prompt):
    pipeline = AutoPipelineForText2Image.from_pretrained(
        pretrained_model, 
        torch_dtype=torch.float16, 
        safety_checker=None, 
        requires_safety_checker=False
    ).to("cuda")

    prompt = user_prompt

    generated_image = pipeline(prompt, num_inference_steps=steps).images[0]

    generated_image.save(path_images)
    #plt.imshow(generated_image)
    #plt.show()
