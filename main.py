from mongoengine import connect
from fastapi import FastAPI, APIRouter
from song.routes import songs
from user.routes import user
from playlist.routes import playlsit
connect(db="SocialMedia", alias="db1", host="mongodb+srv://avbigbuddy:nZ4ATPTwJjzYnm20@cluster0.wplpkxz.mongodb.net/SocialMedia")

# Connect tomu the second database
connect(db="songapp", alias="db2", host="mongodb+srv://avbigbuddy:nZ4ATPTwJjzYnm20@cluster0.wplpkxz.mongodb.net/songapp")

app = FastAPI()
app.include_router(songs.router, tags=["songs Apis"])
app.include_router(user.router, tags=["user Apis"])
app.include_router(playlsit.router, tags=["playlist Apis"])