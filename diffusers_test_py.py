from diffusers import AutoPipelineForText2Image
import torch
from matplotlib import pyplot as plt

pipeline = AutoPipelineForText2Image.from_pretrained(
    "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16, safety_checker = None, requires_safety_checker = False
).to("cuda")

prompt = "green car"

image = pipeline(prompt, num_inference_steps=2).images[0]
plt.imshow(image)