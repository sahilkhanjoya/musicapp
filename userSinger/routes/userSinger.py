from userSinger.model.userSingermodel import UserSelectSingerModel, UserSelectSingerTable
from fastapi import APIRouter, HTTPException, Query

import json
from mongoengine import Q
from pydantic import BaseModel
from collections import Counter
from artiis.model.artistmodel import ArtistModel, ArtistTableOrLibrariy
from bson import ObjectId
router = APIRouter()
@router.post("/api/v1/add-artist-for-user")
async def addArtistForUser(body: UserSelectSingerModel):
    saveData = UserSelectSingerTable(**body.dict())
    saveData.save()
    tojson = saveData.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Success",
        "data":fromjson,
        "status":True
    }
@router.delete("/api/v1/add-artist-for-user/{artistID}/{userid}")
async def addArtistForUser(artistID: str, userid: str):
    saveData = UserSelectSingerTable.objects(artistID=artistID, userid=userid).first()
    saveData.delete()
    return {
        "message":"Deletation Success",
        "status":True
    }
    
@router.get("/api/v1/get-artist-by-userid/{userid}")
async def addArtistForUser( userid: str):
    artistslist = []
    saveData = UserSelectSingerTable.objects( userid=userid).all()
    for v in saveData:
        artist = ArtistTableOrLibrariy.objects.get(id=ObjectId(v.artistID))
        tojson = artist.to_json()
        fromjson = json.loads(tojson)
        artistslist.append(fromjson)
    return {
        "message":"here is all singer Success",
        "data": artistslist,
        "status":True
    }