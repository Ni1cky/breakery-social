from datetime import datetime
import requests

from controllers.authorization import send
from views.meta import HOST
from store.models.models import Message, MessageCreate


# def get_message(message_id: int):
#     response = requests.get(f"{HOST.URL}/messages/{message_id}")
#     message = Message(**(response.json()))
#     return message


def get_messages_for_dialogue(user1_id: int, user2_id: int):
    req = requests.Request('GET', f"{HOST.URL}/messages/{user2_id}")
    response = send(req)
    messages = [Message(**message_params) for message_params in response.json()]

    return messages


def get_time_send_sorted_message(sender_id: int, recipient_id: int):
    messages = get_messages_for_dialogue(sender_id, recipient_id)
    sorted_messages = sorted(messages,
                             key=lambda message: datetime.strptime(str(message.time_send), "%Y-%m-%d %H:%M:%S.%f"))
    return sorted_messages


def create_message(message: MessageCreate):
    params = message.dict()
    params["time_send"] = str(params["time_send"])
    #requests.post(f"{HOST.URL}/messages", json=params)
    req = requests.Request('POST', f"{HOST.URL}/messages", json=params)
    response = send(req)
