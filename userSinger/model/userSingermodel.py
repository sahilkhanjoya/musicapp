from pydantic import BaseModel
from mongoengine import Document, StringField

class UserSelectSingerTable(Document):
    userid =StringField(required=True)
    artistID = StringField(required=True)
    meta = {'db_alias': 'db2'}
class UserSelectSingerModel(BaseModel):
    userid: str
    artistID: str