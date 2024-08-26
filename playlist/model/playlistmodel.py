from mongoengine import Document, StringField, IntField, BooleanField, ListField, DateTimeField
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PlaylistTable(Document):
    name = StringField(required=True)
    userid = StringField(required=True)
    meta = {'db_alias': 'db2'}
    
class PlaylisModel(BaseModel):
    name : str
    userid : str
    
class PLaylistSongTable(Document):
    playlistidID = StringField(required=True)
    songid = StringField(required=True)
    meta = {'db_alias': 'db2'}
    
class PLaylistSongModel(BaseModel):
    playlistidID : str
    songid : str
    