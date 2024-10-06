from fastapi import APIRouter
from user.models.usermodel import UserModel, UserTabel
import json
router = APIRouter()

@router.post("/api/v1/user-create-login")
async def getAllSongs(body: UserModel):
    finduser = UserTabel.objects(identifyer=body.identifyer)
    if finduser :
        tojson = finduser.to_json()
        fromjson = json.loads(tojson)
        return {
            "message": "User Login succes",
            "data":fromjson,
            "status":True
        }
        
    else:
        saveuser = UserTabel(**body.dict())
        saveuser.save()
        tojson = saveuser.to_json()
        fromjson = json.loads(tojson)
        return {
            "message": "User create succes",
            "data":fromjson,
            "status":True
        }
        

