import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    login: str
    hash_pass: str
    name: str
    surname: str
    photo: str
    additional_data: str


class Message(BaseModel):
    text: str
    time_send: datetime.datetime
    is_read: bool
    is_important: bool
    is_edited: bool

class Post(BaseModel):
    text: str
    author: str
    time_send: datetime.datetime
