import requests

from controllers.authorization import send
from store.models.models import Dialog, DialogCreate
from views.meta import HOST


def get_dialog_by_id(dialog_id: int):
    req = requests.Request('GET', f"{HOST.URL}/dialogs/{dialog_id}")
    response = send(req)
    #response = requests.get(f"{HOST.URL}/dialogs/{dialog_id}")
    dialog = Dialog(**response.json())
    return dialog


def create_dialog(dialog: DialogCreate):
    req = requests.Request('POST', f"{HOST.URL}/dialogs", json=dialog.dict())
    response = send(req)
    #return requests.post(f"{HOST.URL}/dialogs", json=dialog.dict())
    return response


def get_dialog_by_users_ids(user1_id: int, user2_id: int):
    req = requests.Request('GET', f"{HOST.URL}/dialogs/{user1_id}/{user2_id}")
    response = send(req)
    #response = requests.get(f"{HOST.URL}/dialogs/{user1_id}/{user2_id}")
    dialog = Dialog(**response.json())
    return dialog


def get_users_dialogs(user_id: int):
    req = requests.Request('GET', f"{HOST.URL}/dialogs/all/{user_id}")
    response = send(req)
    #response = requests.get(f"{HOST.URL}/dialogs/all/{user_id}")
    dialogs = [Dialog(**d) for d in response.json()]
    return dialogs
