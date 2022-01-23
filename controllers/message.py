from datetime import datetime
import requests
from store.models.models import Message, MessageCreate


def get_message(message_id: int):
    response = requests.get(f"http://127.0.0.1:8000/messages/{message_id}")
    message = Message(**(response.json()))
    return message


def get_messages_for_dialogue(user1_id: int, user2_id: int):
    response = requests.get(f"http://127.0.0.1:8000/messages/{user1_id}/{user2_id}")
    messages = [Message(**message_params) for message_params in response.json()]
    return messages


def get_time_send_sorted_message(sender_id: int, recipient_id: int):
    messages = get_messages_for_dialogue(sender_id, recipient_id)
    sorted_messages = sorted(messages,
                             key=lambda message: datetime.strptime(str(message.time_send), "%Y-%m-%d %H:%M:%S.%f"),
                             reverse=True)
    return sorted_messages


def create_message(message: MessageCreate):
    requests.post("http://127.0.0.1:8000/messages", json=message.dict())
