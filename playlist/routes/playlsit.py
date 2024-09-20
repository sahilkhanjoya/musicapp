from fastapi import APIRouter, Query
from song.models.songstable import SongsModel, SongsTable
from song.models.liketable import LikeSongModel, LikeSongTable
from playlist.model.playlistmodel import PlaylisModel, PlaylistTable, PLaylistSongModel, PLaylistSongTable
import json
from bson import ObjectId
router = APIRouter()

@router.post("/api/v1/create-playlist")
async def createPlaylist(body: PlaylisModel):
    savedata = PlaylistTable(**body.dict())
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
    savedata = PLaylistSongTable(**body.dict())
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
    savedata.delete()
    tojson = savedata.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"sond delet",
        "data": fromjson,
        "status" : True
    }

@router.get("/api/v1/get-playlist-song-for-home")
async def getPLaylist(limit: int = Query(10, ge=1), offset: int = Query(0, ge=0)):
    array = []
    findPlaylist = PlaylistTable.objects.skip(offset).limit(limit).all()
    for value in findPlaylist:
        findsong = PLaylistSongTable.objects(playlistidID=ObjectId(value.playlistidID)).skip(0).limit(limit).all()


    tojson = findPlaylist.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Here is the Playlist",
        "data": fromjson,
        "status":True
    }


@router.get("/api/v1/get-user-playlist/{userid}")
def getUserPlaylist(userid: str):
    playlistsong = []
    findPlaylist = PlaylistTable.objects(userid=userid).all()
    if findPlaylist:
        for v in findPlaylist:
            findalsongs = PLaylistSongTable.objects(playlistidID=ObjectId(v.id))
            songs = []
            for songid in findalsongs:
                song = SongsTable.objects.get(id=ObjectId(songid.songid))
                tojson = song.to_json()
                fromjon = json.loads(tojson)
                songs.append(fromjon)
            playlistsong.append(songs)
        return {
            "message":"Here is your all playlist and song",
            "data":playlistsong,
            "status":True
        }
    else:
        return {
            "message":"Playlist not found",
            "data": None,
            "status":False
        }

    
    