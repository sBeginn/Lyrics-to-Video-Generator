from __future__ import print_function
import cv2 as cv
import numpy as np
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import function_images_to_video
import function_generate_images

#Spotify API-Zugangsdaten
SPOTIPY_CLIENT_ID = 'e1fd87ab69f3494c8955baf382855de8'
SPOTIPY_CLIENT_SECRET = 'a29340abbe9d495aa77f88ae96da3e12'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'

#Authentifizierung
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope='user-library-read'))

current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, "generated_images")

width_image = 3840
height_image = 2160
resize_factor = 2


def generate_rotated_images(samples_warp):
    for file_name in os.listdir(images_path):
        if file_name.endswith(('.jpg', '.jpeg', '.png')):
            # Lade das Bild
            img_path = os.path.join(images_path, file_name)
            img = cv.imread(img_path)

            # Ändere die Größe des Eingangsbildes
            img = cv.resize(img, (int(img.shape[1] * resize_factor), int(img.shape[0] * resize_factor)))

            # Erstelle ein leeres Bild mit konstanter Größe und schwarzen Hintergrund
            canvas = np.zeros((height_image, width_image, 3), dtype=np.uint8)

            # Berechne die Position, um das ursprüngliche Bild in der Mitte zu platzieren
            x_offset = (width_image - img.shape[1]) // 2
            y_offset = (height_image - img.shape[0]) // 2

            # Füge das ursprüngliche Bild in das leere Bild ein
            canvas[y_offset:y_offset + img.shape[0], x_offset:x_offset + img.shape[1]] = img

            # Speichere das ursprüngliche Bild mit schwarzem Hintergrund
            original_file = os.path.join(current_path, "generated_images", f'{file_name}_original.png')
            cv.imwrite(original_file, canvas)

            # Erstelle die festgelegte Anzahl von Rotationen für jedes Bild
            for i in range(samples_warp):
                # Definiere die Rotation und Skalierung
                angle = i * (360 / samples_warp)  # Änderung der Richtung

                # Transformationsmatrix für die Affine Transformation
                rot_mat = cv.getRotationMatrix2D((width_image // 2, height_image // 2), angle, 1.0)

                # Anwenden der Affine Transformation
                rotated_img = cv.warpAffine(canvas, rot_mat, (width_image, height_image))

                # Speichere das resultierende Bild im Ordner "generated_images"
                output_file = os.path.join(current_path, "generated_images", f'{file_name}_rotation_{i+1:04d}.png')
                cv.imwrite(output_file, rotated_img)

            # Lösche das ursprüngliche Bild
            os.remove(img_path)
        
def song_duration(input_songname, input_artist):
    
    song_name = input_songname
    artist_name = input_artist

    results = sp.search(q=f'track:{song_name} artist:{artist_name}', type='track', limit=1)

    if results['tracks']['items']:
        track_info = results['tracks']['items'][0]
        track_id = track_info['id']
        
        duration_ms = track_info['duration_ms']
        duration_sec = duration_ms // 1000
        
        samples_warp = int((duration_sec * function_images_to_video.fps) / (function_generate_images.samples * 3))

        return samples_warp 
    else:
        print(f'Kein Song mit dem Titel "{song_name}" von {artist_name} gefunden.')




       




