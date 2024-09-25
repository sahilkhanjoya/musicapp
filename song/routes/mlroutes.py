from fastapi import APIRouter, HTTPException, Query
from song.routes.ml.promptextracter import customNLP
router = APIRouter()

@router.get("/api/v1/ml-data/{query}")
async def getMLDAta(query: str):
    data = customNLP(query)
    return {
        "message": data
    }