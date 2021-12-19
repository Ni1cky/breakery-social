import requests
from store.models.models import User


def get_users():
    response = requests.get("http://127.0.0.1:8000/users")
    users = [User(**user_params) for user_params in response.json()]
    return users


def get_user(user_id):
    user = User(**requests.get(f"http://127.0.0.1:8000/users/{user_id}").json())
    return user
