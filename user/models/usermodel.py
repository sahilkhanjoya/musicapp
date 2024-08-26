from mongoengine import Document, StringField, IntField, BooleanField, ListField, DateTimeField
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserTabel(Document):
    identifyer = StringField(required=True)
    name = StringField(required=True)
    mailorphone = StringField(required=True)
    meta = {'db_alias': 'db2'}
class UserModel(BaseModel):
    identifyer : str
    name : str
    mailorphone : str