import requests


def get_users():
    users = requests.get("http://127.0.0.1:8000/users").json()
    return users
