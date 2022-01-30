import requests
from store.models.models import Dialog, DialogCreate
from views.meta import HOST


def get_dialog_by_id(dialog_id: int):
    response = requests.get(f"{HOST.URL}/dialogs/{dialog_id}")
    dialog = Dialog(**response.json())
    return dialog


def create_dialog(dialog: DialogCreate):
    return requests.post(f"{HOST.URL}/dialogs", json=dialog.dict())


def get_dialog_by_users_ids(user1_id: int, user2_id: int):
    response = requests.get(f"{HOST.URL}/dialogs/{user1_id}/{user2_id}")
    dialog = Dialog(**response.json())
    return dialog
