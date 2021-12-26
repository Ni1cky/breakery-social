import datetime
from typing import List
from pydantic import BaseModel


class PostBase(BaseModel):
    text: str
    time_created: datetime.datetime
    author_id: int


class Post(PostBase):
    id: int


class PostCreate(PostBase):
    pass


class UserBase(BaseModel):
    login: str
    hash_pass: str
    name: str
    surname: str
    photo: str
    additional_data: str
    posts: List[Post]


class User(UserBase):
    id: int


class UserCreate(UserBase):
    pass


class MessageBase(BaseModel):
    text: str
    time_send: datetime.datetime
    is_read: bool
    is_important: bool
    is_edited: bool
    sender_id: int
    receiver_id: int


class Message(MessageBase):
    id: int
    send_from_me: bool


class MessageCreate(MessageBase):
    pass


class PostBase(BaseModel):
    text: str
    author: str
    time_send: datetime.datetime


class Post(PostBase):
    id: int


class PostCreate(BaseModel):
    pass
