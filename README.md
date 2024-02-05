# Lyrics2Video Generator

With this repository you can automatically receive a generated music video in a very short time by entering a song name. the artist and a YouTube Link.

## **Installation (takes 5-10 minutes)**

First, you need to clone the respoitory:
```
git clone https://github.com/sBeginn/Lyrics-to-Video-Generator.git
```

Then open the command prompt and enter the path to the folder:
```
cd path\to\folder
```

After that you can install the necessary libraries:
```
pip install -r requirements.txt
```
#### Genius connection:
- Go to ```https://genius.com/api-clients``` and create account or log in
- Now click on "New API Client" and enter the information (It is not relevant what you enter there)
- After this click on "Generate Access Token" and copy the token
- Enter this token in the file **function_read_lyrics.py** in the variable ```token = ``` in line 9

#### Spotify connection:
- Go to ```https://developer.spotify.com/``` and create Account or log in
- Go to ```https://developer.spotify.com/dashboard``` and click on "create app" and enter in Redirect URI: "http://localhost:3000" and enter the other information (This information are also not relevant)
- After this click on "settings" and copy the Client ID and Client Secret.
- Open the file **function_warp_affine.py** and enter the tokens:
  - Client ID in variable ``` SPOTIPY_CLIENT_ID =``` in line 10
  - Client Secret in variable ```SPOTIPY_CLIENT_SECRET =``` in line 11
  - Redirect URI in variable ```SPOTIPY_REDIRECT_URI = http://localhost:3000 ``` in line 12 (or change http://localhost:3000 with that what you enter in the spotify app information)
  
**Installation complete**


## **Run**

Run **main.py** and you can enter in the terminal the following information:
  - Songname (complete songname, but capitalization doesn't matter)
  - Artist (If several -> Normally one artist is enough)
  - URL (Enter a URL from Youtube of this song, so the generated video has the fitting song as a audio)

When it is finished -> You will find your video in the folder "generated_video"

