import cv2 as cv
import numpy as np
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import function_images_to_video
import function_generate_images
import random

# Conncetion to spotipy (Enter your own tokens)
SPOTIPY_CLIENT_ID = 'e1fd87ab69f3494c8955baf382855de8'
SPOTIPY_CLIENT_SECRET = 'a29340abbe9d495aa77f88ae96da3e12'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'

# Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope='user-library-read'))

# Path to current file
current_path = os.path.dirname(__file__)

# Path to images folder
images_path = os.path.join(current_path, "generated_images")

# Width & height of the image
width_image = 3840
height_image = 2160

# Size of the image
resize_factor = 3

# Function to generate the rotation images (samples_warp is define in the function song_duration)
def generate_rotated_images(samples_warp):
    
    # Loop for every generated image in the folder
    for file_name in os.listdir(images_path):
        
        # Check if the file is a image
        if file_name.endswith(('.jpg', '.jpeg', '.png')):
            
            # Load th eimage
            img_path = os.path.join(images_path, file_name)
            img = cv.imread(img_path)

            # Change the size of the inout image
            img = cv.resize(img, (int(img.shape[1] * resize_factor), int(img.shape[0] * resize_factor)))

            # Create a background image with random color
            canvas = np.zeros((height_image, width_image, 3), dtype=np.uint8)
            random_background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            canvas[:, :] = random_background_color

            # Position for the input image in the middle
            x_offset = (width_image - img.shape[1]) // 2
            y_offset = (height_image - img.shape[0]) // 2

            # Put the input image in the image with random background color
            canvas[y_offset:y_offset + img.shape[0], x_offset:x_offset + img.shape[1]] = img

            # Save the images
            original_file = os.path.join(current_path, "generated_images", f'{file_name}_original.png')
            cv.imwrite(original_file, canvas)

            # Loop for the range of the rotated images
            for i in range(samples_warp):
                # Define the rotation 
                angle = i * (360 / samples_warp)  

                # Transformation matrix
                rot_mat = cv.getRotationMatrix2D((width_image // 2, height_image // 2), angle, 1.0)

                # Use warp affine 
                rotated_img = cv.warpAffine(canvas, rot_mat, (width_image, height_image))

                # Calculate for the transition image in the background
                alpha = i / samples_warp
               
                # Corssfades the rotated image
                blended_img = cv.addWeighted(rotated_img, alpha, canvas, 1 - alpha, 0)

                # Save the images in the images folder
                output_file = os.path.join(current_path, "generated_images", f'{file_name}_rotation_{i+1:04d}.png')
                cv.imwrite(output_file, blended_img)

            # Delete the input images
            os.remove(img_path)


# Function to calculate the song duration
def song_duration(input_songname, input_artist):

    song_name = input_songname
    artist_name = input_artist

    # Search the input song
    results = sp.search(q=f'track:{song_name} artist:{artist_name}', type='track', limit=1)

    # Check to find the right song
    if results['tracks']['items']:
        track_info = results['tracks']['items'][0]
        track_id = track_info['id']
        
        # Song duration in milliseconds
        duration_ms = track_info['duration_ms']
        
        # Song duration in seconds
        duration_sec = duration_ms // 1000
        
        # Calculate the number of images that need to be generated -> It is important because we want that the video has the same length as the song 
        samples_warp = int((duration_sec * function_images_to_video.fps) / (function_generate_images.samples * 3))

        # Return the number
        return samples_warp
    
    else:
        print(f'No Song found')
