from fastapi import APIRouter
import json
from song.models.songstable import SongsTable
import random
from mongoengine import Q
import pandas as pd
from song.routes.ml.songsml import search_songs_by_prompt
from song.routes.ml.ml import suggest_song
from song.routes.ml.lyrcsto_song import find_song_by_lyrics
router = APIRouter()

with open('song/routes/singerjson.json', 'r') as file:
    data = json.load(file)


#play venom by blackpink
#play anuv jain's songs


@router.get('/api/v1/get-recomidation-song/{singername}')
async def recomidationSong(singername: str):
    parts = singername.split(" | ")
    allsongs = []
    if 'singers' in data:
    # Search for the name in the list
       result = next((singer for singer in data['singers'] if singer['name'] == parts[0]), None)
    
    # Print the result if found
       if result:
        
        singersList = []
        for v in result['emotions']:
          for i in data['singers']:
             for emotion in i["emotions"]:
                if (emotion == v):
                   singersList.append(i)
        for singer in singersList:
            songs = SongsTable.objects(singer__icontains =singer['name']).all()
            if songs:
               for onesong in songs:
                  tosong = onesong.to_json()
                  fromsong = json.loads(tosong)
                  allsongs.append(fromsong)
               
            else:
              print(f"not found {singer['name']}")


       else:
          print(f"{singername} not found in the data.")
       return {
          "query": singername,
          "message":"Here is all suggestion songs",
          "data": allsongs,
          "status":True
       }
    else:
         return {
          "query": singername,
          "message":"Here is all suggestion songs",
          "data": None,
          "status":False
       }
         

# FastAPI route for handling song search

@router.get("/api/v1/getsongs-byspeec/{query}")
async def get_songs_by_speech(query: str):
   songs = suggest_song(query)
   songslist = []
   if songs["data"] == None and songs["status"] == None:
      return {
         "message": "Sorry i cant find",
         "data":None,
         "status":False
       }
   elif songs["data"] != None and songs["status"]==True:
       for value in songs["data"]:
          
          perticulersong  = SongsTable.objects(Name__icontains=value["song_name"])
          tojson = perticulersong.to_json()
          fromjson = json.loads(tojson)
          songslist.append(fromjson)
   elif songs["data"] != None and songs["status"] == False:
         return songs
   return {
             "message":"Here is songs according to you",
             "data" : songslist,
             "status":True
          }
   
@router.get("/api/v1/search-song-by/{lyrcs}")
async def searchSongBy(lyrcs: str):
  
   if "play" in lyrcs or "from" in lyrcs or any(emotion in lyrcs for emotion in ["sad", "happy", "romantic", "party"]):
      songs = suggest_song(lyrcs)
      songslist = []
      if songs["data"] == None and songs["status"] == None:
        return {
         "message": "Sorry i cant find",
         "data":None,
         "status":False
       }
      elif songs["data"] != None and songs["status"]==True:
       for value in songs["data"]:
          
          perticulersong  = SongsTable.objects(Name__icontains=value["song_name"]).first()
          tojson = perticulersong.to_json()
          fromjson = json.loads(tojson)
          songslist.append(fromjson)
          
      
      
      return {
             "message":"Here is songs according to you",
             "data" : songslist,
             "status":True
          }
   else:
        data = find_song_by_lyrics(lyrcs)
        if  not data.empty:
           
           
           song_value = data.to_json(orient="records")
           print(song_value)
           songDataJson = json.loads(song_value)
           findSong = SongsTable.objects(Name=songDataJson[0]["songs"])
           tojson  = findSong.to_json()
           fromjson = json.loads(tojson),
           random.shuffle(fromjson)
           return {
            "message": "Song found",
            "data": fromjson[0],
            "staus":True
           }  # Adjust the column names if necessary
        else:
           return {
            "message": "Song not found",
            "data": None,
            "staus":False
           }
     