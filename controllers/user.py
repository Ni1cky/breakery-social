import requests
from store.models.models import User
from views.meta import HOST

USERS_BLOCK_SIZE = 25


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
    response = requests.get(f"{HOST.URL}/users/me")
    user = User(**response.json())
    return user


def update_user(user: dict):
    requests.put(f'{HOST.URL}/users/{user["id"]}/edit', json=user)


def get_block_of_all_users(min_id: int):
    max_id = min_id + USERS_BLOCK_SIZE
    block = requests.get(f"{HOST.URL}/users_block", params={'min_id': min_id, 'max_id': max_id}).json()
    return block
