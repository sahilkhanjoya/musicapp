from fastapi import APIRouter, HTTPException, Query
from song.routes.ml.promptextracter import customNLP
from song.models.songstable import SongsTable
import json
router = APIRouter()

@router.get("/api/v1/ml-data/{query}")
async def getMLDAta(query: str):
    data = customNLP(query)
    findsong = SongsTable.objects(Name__icontains=data).first()
    tojson = findsong.to_json()
    fromjson = json.loads(tojson)
    return {
        "message": "here is song",
        "data":fromjson
    }