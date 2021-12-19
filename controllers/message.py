import requests


def get_message(message_id):
    message = requests.get(f"http://127.0.0.1:8000/messages/{message_id}")
    return message


def get_messages_for_dialogue(from_id: int, to_id: int):
    messages = requests.get(f"http://127.0.0.1:8000/messages/{from_id}/{to_id}").json()
    return messages
