import cv2 as cv
import os

current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, "generated_images")

samples = 100

def calc_alpha(samples, current_value):
    start_value = 0.1
    end_value = 1.0
    step_value = (end_value - start_value) / (samples - 1)
    return start_value + current_value * step_value 

width_image = 3840
height_image = 2160

def create_transition(img_transition_1, img_transition_2, output_folder, samples, img_sequence):
    for j in range(samples):
        alpha = calc_alpha(samples, j)
        beta = 1.0 - alpha
        dst = cv.addWeighted(img_transition_1, alpha, img_transition_2, beta, 0.0)
        output_path = os.path.join(output_folder, f"transition_{img_sequence}_{j}.png")
        cv.imwrite(output_path, dst)

def transitions(samples):
    images_array = []

    for image_file in sorted(os.listdir(images_path)):
        image_path = os.path.join(images_path, image_file)
        images_array.append(image_path)

    for i in range(len(images_array)-1):
        img_transition_1 = cv.imread(images_array[i+1])
        img_transition_2 = cv.imread(images_array[i])

        img_transition_1 = cv.resize(img_transition_1, (width_image, height_image))
        img_transition_2 = cv.resize(img_transition_2, (width_image, height_image))

        create_transition(img_transition_1, img_transition_2, images_path, samples, f"{i}-{i+1}")

    #löscht ausgangsbilder
    for image_file in images_array:
        os.remove(image_file)


