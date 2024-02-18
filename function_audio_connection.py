from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os

# Path to the current file 
current_path = os.path.dirname(__file__)

# Path to video folder
folder_video_path = current_path + "/generated_video"

# Path to video file
video_path = current_path + "/generated_video/output_video.mp4"

# Path to audio file
audio_path = current_path + "/generated_video/output_audio.mp4"

# Path to finished video file
finished_video_path = current_path + "/generated_video/output_finished_video.mp4"

# Function to download the audio for the song
def download_audio(input_url):
    
    # Connection to youtube
    yt = YouTube(input_url)
    stream = yt.streams.get_by_itag(140)
    stream.download(output_path=folder_video_path,filename="output_audio.mp4") # Download only the audio in mp4 format

# Function to connect the audio with generated video
def audio_with_video_connection():
    
    video = VideoFileClip(video_path) # Video
    audio = AudioFileClip(audio_path) # Audio
    
    # Connceted audio with the video
    finished_video = video.set_audio(audio) 
    finished_video.write_videofile(finished_video_path, codec='libx264', audio_codec='aac')
    
    # Remove separate audio and video
    os.remove(video_path)
    os.remove(audio_path)
    
    

   
   
  
     
    
    