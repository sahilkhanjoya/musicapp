from fastapi import APIRouter, HTTPException, Query
from song.models.songstable import SongsModel, SongsTable
from song.models.liketable import LikeSongModel, LikeSongTable
from playlist.model.playlistmodel import PlaylisModel, PlaylistTable, PLaylistSongModel, PLaylistSongTable
import json
from typing import List
import re
from mongoengine import Q
from pydantic import BaseModel
from collections import Counter
from song.routes.ml.suggestionsong import get_recommendations
import random
router = APIRouter()


@router.get("/api/v1/get-song")
async def getAllSongs():
    songs = SongsTable.objects.all()
    tojson = songs.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Here is songs",
        "data":fromjson,
        "status":True
    }

@router.post("/api/v1/like")
async def likeSong(body: LikeSongModel):
    finddata = LikeSongTable.objects(songid=body.songid, userid = body.userid)
    if finddata:
        finddata.delete()
        return {
            "message": "unlike success",
            "status":True
        }
    else :
        savedata = LikeSongTable(body.dict())
        savedata.save()
        return {
            "message": "like success",
            "status":True
        }

@router.get("/api/v1/singer-list")
async def getSinger():
    rawsinger = []
    findsongs = SongsTable.objects.all()
    for v in findsongs:
        separated_list = re.split(r'\s*\|\s*|\s*-\s*', str(v.singer))
        separated_list = [item for item in separated_list if item]
        rawsinger.append(separated_list[0])
        
    string_counts = Counter(rawsinger)
    duplicates = [string for string, count in string_counts.items() if count > 1]
    sorted_names = sorted([name.strip() for name in duplicates], key=str.lower)
    
    return {
        "message":"here is the singers",
        "data":sorted_names,
        "status":True
    }


class SingerSearch(BaseModel):
    singername: str
    
@router.post("/api/v1/get-song", )
async def getSonge(body: SingerSearch, limit: int = Query(10, ge=1), offset: int = Query(0, ge=0)):
    try:
        # Query the database for songs matching the singer name, with pagination
        findata = SongsTable.objects(singer__icontains=body.singername.replace(",", "")).skip(offset).limit(limit).all()

        if not findata:
            raise HTTPException(status_code=404, detail="No songs found for the given singer")

        # Convert the MongoEngine documents to a list of SongResponse models
        
        tojson = findata.to_json()
        fromjson = json.loads(tojson)
        random.shuffle(fromjson)
        return {
            "message":"here is songs",
            "data": fromjson,
            "status" : True
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/v1/get-search/{singername}")
async def getsearcSonge(singername: str):
    try:
        # Query the database for songs matching the singer name, with pagination
        findata = SongsTable.objects(Q(singer__icontains=singername) | Q(Name__icontains=singername)).all()

        if not findata:
            findata = PlaylistTable.objects(name__icontains=singername).all()      # Convert the MongoEngine documensts to a list of SongResponse models
        
        tojson = findata.to_json()
        fromjson = json.loads(tojson)
        
        return {
            "message":"here is songs",
            "data": fromjson,
            "status" : True
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/api/v1/suggestionsong/{currentsongname}")
async def sugggestionson(currentsongname: str):
    recommended_songs = get_recommendations(currentsongname)
    songs = []
    for name in recommended_songs:
        findSong = SongsTable.objects(Name__icontains=name).first()
        tojson = findSong.to_json()
        fromjson = json.loads(tojson)
        songs.append(fromjson)
    return {
        "message":"Here is Suggestion Songs",
        "data" : songs,
        "status": True
    }