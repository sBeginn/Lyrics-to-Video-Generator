import cv2
import os

# Path to current file
current_path = os.path.dirname(__file__)

# Path to images folder
path_images = current_path + "/generated_images"

# Path to the output video
path_video = current_path + "/generated_video/output_video.mp4"

# Information about the images
width_image = 3840
height_image = 2160

# Number of frames pro second (Recommendation: > 10)
fps = 20

# Function to generate the video
def generate_video():
    
    # Create a list
    images_array = []

    # Loop for all images in the folder 
    for image_file in sorted(os.listdir(path_images)):
        image_path = os.path.join(path_images, image_file)
        images_array.append(image_path) # Add the images to the list

    if not images_array:
        print("No generated images")
        return

    # Generate video in .mp4 format
    created_video = cv2.VideoWriter(path_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width_image, height_image))

    # Loop for all images in the list
    for image in images_array:
        img_read = cv2.imread(image) # Read the image
        img_resize = cv2.resize(img_read, (width_image, height_image)) # Resize the image
        created_video.write(img_resize) # Write the image in the video

    created_video.release() # Video is completed

    # Remove the images in the folder
    for image in images_array:
        os.remove(image)

