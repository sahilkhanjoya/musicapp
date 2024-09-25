import pandas as pd
from song.models.songstable import SongsTable
import json
df = pd.read_csv('song/routes/data/trainsongdata - Sheet1.csv')
def clearNullValue():
   df = df.dropna()
   
def getSongsByEmotion(emotion):
    df.columns = df.columns.str.strip()
    filtered_data = df[df['emotion'] == emotion]
    print(filtered_data[['songs', 'singer', 'movie', 'rating']])
    a = filtered_data.to_json(orient='records',indent=4)
    b = json.loads(a)
    return b[0]["songs"]
   
def getSongbySingerSong(singer, song):
    df.columns = df.columns.str.strip()
    data = df[df['songs'].str.contains(song, case=False, na=False) & df['singer'].str.contains(singer, case=False, na=False)]
    a = data.to_json(orient='records', indent=4)
    b = json.loads(a)
    return b[0]["songs"]

def playsongbySinger(singer):
    songs = df[df['singer'].str.contains(singer, case=False, na=False)]
    tojson = songs.to_json(orient='records', indent=4)
    fromjson = json.loads(tojson)
    return fromjson[0]["songs"]

def playsongFromMovie(song, movie):
   df.columns = df.columns.str.strip()
   songdata = df[df['songs'].str.contains(song, case=False, na=False) & df['movie'].str.contains(movie, case=False, na=False)]
   tojson = songdata.to_json(orient='records', indent=4)
   fromjson = json.loads(tojson)
   return fromjson[0]["songs"]

def searchSongBySongName(songname):
   df.columns = df.columns.str.strip()
   song = df[df['songs'].str.contains(songname, case=False, na=False)]
   a = song.to_json(orient='records', indent=4)
   fromjson = json.loads(a)
   return fromjson[0]["songs"]

def toRatingSongsbyEmotion(emotion):
   df.columns = df.columns.str.strip()
   df['rating'] = df['rating'].str.replace(',', '').astype(float)
   emotion_filtered = df[df['emotion'].str.lower() == emotion.lower()]
   best_song = emotion_filtered.loc[emotion_filtered['rating'].idxmax()]
   print(best_song[['songs', 'singer', 'movie', 'rating']])
   tojson = best_song[['songs', 'singer', 'movie', 'rating']].to_json(orient='records')
   fromjson = json.loads(tojson)
   return fromjson
   
def suggestmemostEmotionongsBySinger(emotion, singer):
   df.columns = df.columns.str.strip()
   df['rating'] = pd.to_numeric(df['rating'].astype(str).str.replace(',', ''), errors='coerce')
   emotion_filtered = df[(df['emotion'].str.lower() == 'sad') & (df['singer'].str.lower().str.contains(singer.lower()))]
   emotion_filtered = emotion_filtered.dropna(subset=['rating'])
   if not emotion_filtered.empty:
        # Find the song with the highest rating for the specified singer and emotion
        best_song = emotion_filtered.loc[emotion_filtered['rating'].idxmax()]
        tojson = best_song[['songs', 'singer', 'movie',]].to_json(orient='records')
        fromjson = json.loads(tojson)
        return fromjson

   else:
        return None
    
    
def searchbyLyrics(lyrcs):
    df.columns = df.columns.str.strip()
    filtered_songs = df[df['lyrics'].str.contains(lyrcs, case=False, na=False)]
    tojson = filtered_songs.to_json(orient='records',indent=4)
    fromjson = json.loads(tojson)
    return fromjson[0]['songs']