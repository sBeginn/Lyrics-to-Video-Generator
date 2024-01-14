from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os


current_path = os.path.dirname(__file__)
folder_video_path = current_path + "/generated_video"
video_path = current_path + "/generated_video/output_video.mp4"
audio_path = current_path + "/generated_video/output_audio.mp4"
finished_video_path = current_path + "/generated_video/output_finished_video.mp4"


def download_audio(input_url):
    yt = YouTube(input_url)
    stream = yt.streams.get_by_itag(140)
    stream.download(output_path=folder_video_path,filename="output_audio.mp4")

def audio_with_video_conncetion():
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path) 
    
    finished_video = video.set_audio(audio)
    finished_video.write_videofile(finished_video_path, codec='libx264', audio_codec='aac')
    os.remove(video_path)
    os.remove(audio_path)
    
    

   
   
  
     
    
    