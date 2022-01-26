from controllers.authorization import get_my_profile
from controllers.user import get_user
import requests


def subscribe_to_user(subscription_id: int):
    me = get_my_profile()
    p = {"subscriber_id": me["id"], "subscription_id": subscription_id}
    requests.post("http://127.0.0.1:8000/subscriptions", params=p)


def unsubscribe_from_user(subscription_id: int):
    me = get_my_profile()
    p = {"subscriber_id": me["id"], "subscription_id": subscription_id}
    requests.delete("http://127.0.0.1:8000/subscriptions", params=p)


def get_subscribers(user_id: int):
    subscribers = requests.get(f"http://127.0.0.1:8000/subscriptions/{user_id}/subscribers").json()
    users = []
    for data in subscribers:
        user = get_user(data['subscriber_id'])
        users.append(user)
    return users


def get_subscriptions(user_id: int):
    subscriptions = requests.get(f"http://127.0.0.1:8000/subscriptions/{user_id}/subscriptions").json()
    users = []
    for data in subscriptions:
        user = get_user(data['user_id'])
        users.append(user)
    return users
