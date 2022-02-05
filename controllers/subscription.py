from controllers.authorization import get_my_profile, send
from controllers.user import get_user
from views.meta import HOST
import requests


def subscribe_to_user(subscription_id: int):
    me = get_my_profile()
    p = {"subscriber_id": me["id"], "subscription_id": subscription_id}
    req = requests.Request('POST', f"{HOST.URL}/subscriptions", params=p)
    resp = send(req).json()
    #requests.post(f"{HOST.URL}/subscriptions", params=p)


def unsubscribe_from_user(subscription_id: int):
    me = get_my_profile()
    p = {"subscriber_id": me["id"], "subscription_id": subscription_id}
    #requests.delete(f"{HOST.URL}/subscriptions", params=p)
    req = requests.Request('DELETE', f"{HOST.URL}/subscriptions", params=p)
    resp = send(req).json()


def get_subscribers(user_id: int):
    req = requests.Request('GET', f"{HOST.URL}/subscriptions/{user_id}/subscribers")
    subscribers = send(req).json()
    #subscribers = requests.get(f"{HOST.URL}/subscriptions/{user_id}/subscribers").json()
    users = []
    for data in subscribers:
        user = get_user(data['subscriber_id'])
        users.append(user)
    return users


def get_subscriptions(user_id: int):
    req = requests.Request('GET', f"{HOST.URL}/subscriptions/{user_id}/subscriptions")
    subscriptions = send(req).json()
    #subscriptions = requests.get(f"{HOST.URL}/subscriptions/{user_id}/subscriptions").json()
    users = []
    for data in subscriptions:
        user = get_user(data['user_id'])
        users.append(user)
    return users


def get_subscriptions_ids(user_id: int):
    req = requests.Request('GET', f"{HOST.URL}/subscriptions/{user_id}/subscriptions")
    subscriptions = send(req).json()
    #subscriptions = requests.get(f"{HOST.URL}/subscriptions/{user_id}/subscriptions").json()
    subscriptions_ids = [s['user_id'] for s in subscriptions]
    return subscriptions_ids


def get_subscribers_ids(user_id: int):
    req = requests.Request('GET', f"{HOST.URL}/subscriptions/{user_id}/subscribers")
    subscribers = send(req).json()
    #subscribers = requests.get(f"{HOST.URL}/subscriptions/{user_id}/subscribers").json()
    subscribers_ids = [s['subscriber_id'] for s in subscribers]
    return subscribers_ids
