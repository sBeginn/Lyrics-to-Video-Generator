# Lyrics2Video Generator

With this repository you can automatically receive a generated music video in a very short time by entering a song name and the artist.

## **Installation**

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
### Genius conncetion:
- Go to ```https://genius.com/api-clients``` and create account or log in
- Now click on "New API Client" and enter the information (It is not relevant what you enter there)
- After this click on "Generate Access Token" and copy the token
- Enter this token in the file function_read_lyrics.py in the variable ```token = ``` in line 9

### Spotify conncetion:
- Go to ```https://developer.spotify.com/``` and create Account or log in
- Go to ```https://developer.spotify.com/dashboard``` and click on "create app" and enter in Redirect URI: "http://localhost:3000" and enter the other information (This information are also not relevant)
- 
  



## **Run**

