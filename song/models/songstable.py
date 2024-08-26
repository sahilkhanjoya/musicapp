from mongoengine import Document, StringField, IntField, BooleanField, ListField, DateTimeField
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SongsTable(Document):
    Name = StringField(required=True)
    image = StringField(required=True)
    songsaudio = StringField(required=True)
    singer = StringField(required=True)
    meta = {'db_alias': 'db1'}


class SongsModel(BaseModel):
    Name : str
    singer:str