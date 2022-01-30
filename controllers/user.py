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


def get_current_user():
    response = requests.get(f"http://127.0.0.1:8000/users/me")
    user = User(**response.json())
    return user
