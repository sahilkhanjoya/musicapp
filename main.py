from mongoengine import connect
from fastapi import FastAPI, APIRouter
from song.routes import songs
from user.routes import user
from playlist.routes import playlsit
from artiis.routes import artitstroutes
from song.routes import suggesationsongroute
from userSinger.routes import userSinger
from song.routes import mlroutes
connect(db="SocialMedia", alias="db1", host="mongodb+srv://avbigbuddy:nZ4ATPTwJjzYnm20@cluster0.wplpkxz.mongodb.net/SocialMedia")

# Connect tomu the second database
connect(db="songapp", alias="db2", host="mongodb+srv://avbigbuddy:nZ4ATPTwJjzYnm20@cluster0.wplpkxz.mongodb.net/songapp")

app = FastAPI()
app.include_router(songs.router, tags=["songs Apis"])
app.include_router(user.router, tags=["user Apis"])
app.include_router(playlsit.router, tags=["playlist Apis"])
app.include_router(artitstroutes.router, tags=["Artist APis"])
app.include_router(suggesationsongroute.router, tags=["Suggestion song"])
app.include_router(userSinger.router, tags=["User Artist"])
app.include_router(mlroutes.router, tags=["ML Artist"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)