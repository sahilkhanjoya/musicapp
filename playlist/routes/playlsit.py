from fastapi import APIRouter
from song.models.songstable import SongsModel, SongsTable
from song.models.liketable import LikeSongModel, LikeSongTable
from playlist.model.playlistmodel import PlaylisModel, PlaylistTable, PLaylistSongModel, PLaylistSongTable
import json
from bson import ObjectId
router = APIRouter()

@router.post("/api/v1/create-playlist")
async def createPlaylist(body: PlaylisModel):
    savedata = PlaylistTable(body.dict())
    savedata.save()
    tojson = savedata.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"playlist created",
        "data": fromjson,
        "status" : True
    }
    
@router.delete("/api/v1/delete-playlist/{id}")
async def createPlaylist(id: str):
    savedata = PlaylistTable.objects.get(id=ObjectId(id))
    savedata.delete()
    tojson = savedata.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"playlist delete",
        "data": fromjson,
        "status" : True
    }

@router.post("/api/v1/create-playlist-addsong")
async def createPlaylist(body: PLaylistSongModel):
    savedata = PLaylistSongTable(body.dict())
    savedata.save()
    tojson = savedata.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"sond added",
        "data": fromjson,
        "status" : True
    }

@router.delete("/api/v1/delet-playlist-addsong/{id}")
async def createPlaylist(body: PLaylistSongModel):
    savedata = PLaylistSongTable.objects.get(id=ObjectId(id)) 
    savedata.save()
    tojson = savedata.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"sond delet",
        "data": fromjson,
        "status" : True
    }
    
    