from mongoengine import Document, StringField, IntField, BooleanField, ListField, DateTimeField
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LikeSongTable(Document):
    songid = StringField(required=True)
    userid = StringField(required=True)
    meta = {'db_alias': 'db2'}
    
class LikeSongModel(BaseModel):
    songid : str
    userid : str