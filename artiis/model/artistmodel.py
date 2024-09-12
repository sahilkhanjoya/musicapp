from mongoengine import Document, StringField, IntField, BooleanField, ListField, DateTimeField
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ArtistTableOrLibrariy(Document):
    name = StringField(required=True)
    image = StringField(required=True)
    meta = {'db_alias': 'db2'}


class ArtistModel(BaseModel):
    name : str