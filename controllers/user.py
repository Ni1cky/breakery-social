import requests
from store.models.models import User
from views.meta import HOST


def get_users():
    response = requests.get(f"{HOST.URL}/users")
    # users = [User(**user_params) for user_params in response.json()]
    users = response.json()
    return users


def get_user(user_id: int):
    response = requests.get(f"{HOST.URL}/users/{user_id}")
    # user = User(**response.json())
    user = response.json()
    return user
