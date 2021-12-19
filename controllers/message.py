import requests
from store.models.models import Message


def get_message(message_id):
    message = Message(**requests.get(f"http://127.0.0.1:8000/messages/{message_id}").json())
    return message


def get_messages_for_dialogue(from_id: int, to_id: int):
    response = requests.get(f"http://127.0.0.1:8000/messages/{from_id}/{to_id}")
    messages = [Message(**message_params) for message_params in response.json()]
    return messages
