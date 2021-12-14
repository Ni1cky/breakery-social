from pydantic import BaseModel

class User(BaseModel):
    id = -1
    login = ''
    hash_pass = ''
    name = ''
    surname = ''
    photo = ''
    additional_data = ''


class Message(BaseModel):
    text = ''
    time_send = ''
    is_read = False
    is_important = False
    is_edited = False