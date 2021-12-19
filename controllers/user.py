import requests


def get_users():
    users = requests.get("http://127.0.0.1:8000/users").json()
    return users


def get_user(user_id):
    user = requests.get(f"http://127.0.0.1:8000/users/{user_id}").json()
    return user
