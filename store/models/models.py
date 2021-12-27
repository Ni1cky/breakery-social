import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    login: str
    password_hash: str
    name: str
    surname: str
    photo: str
    additional_data: str


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


class Message(MessageBase):
    id: int
    send_from_me: int


class MessageCreate(MessageBase):
    pass
