import requests
from store.models.models import Message


def get_message(message_id: int):
    response = requests.get(f"http://127.0.0.1:8000/messages/{message_id}")
    message = Message(**(response.json()))
    return message


def get_messages_for_dialogue(user1_id: int, user2_id: int):
    response = requests.get(f"http://127.0.0.1:8000/messages/{user1_id}/{user2_id}")
    messages = [Message(**message_params) for message_params in response.json()]
    return messages
