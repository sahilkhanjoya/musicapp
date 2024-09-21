from fastapi import APIRouter
import json
from song.models.songstable import SongsTable
from mongoengine import Q
import pandas as pd
from song.routes.ml.songsml import search_songs_by_prompt
from song.routes.ml.ml import suggest_song
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
    return {"data": songs}