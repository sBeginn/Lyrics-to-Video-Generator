import cv2
import os

current_path = os.path.dirname(__file__)
path_images = current_path + "/generated_images"

path_video = current_path + "/generated_video/output_video.mp4"

width_image = 3840
height_image = 2160
fps = 1

def generate_video():
    images_array = []

    for image_file in os.listdir(path_images):
        image_path = os.path.join(path_images, image_file)
        images_array.append(image_path)

    if not images_array:
        print("No generated images")
        return

    created_video = cv2.VideoWriter(path_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width_image, height_image))

    for image in images_array:
        img_read = cv2.imread(image)
        img_resize = cv2.resize(img_read, (width_image, height_image))
        created_video.write(img_resize)

    created_video.release()

    for image in images_array:
        os.remove(image)
        
generate_video()




