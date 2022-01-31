import datetime
import requests

from views.meta import HOST
from controllers.photo import add_post_picture
from controllers.subscription import get_subscriptions
from controllers.user import get_users, get_user

DATE_FORMAT = "%d %b %y  %H:%M"


def add_post(user_id: int, text: str, time_created: str, path_to_image: str):
    r = requests.post(f"{HOST.URL}/newpost", json={'author_id': user_id, 'text': text, 'time_created': time_created})
    post_id = r.json()
    add_post_picture(user_id, post_id, path_to_image)


def sort_posts(posts: list):
    return sorted(posts, key=lambda x: datetime.datetime.strptime(x['time_created'], DATE_FORMAT), reverse=True)


def get_sorted_user_posts(user_id: int):
    posts = requests.get(f"{HOST.URL}/posts/{user_id}/all").json()
    posts = sort_posts(posts)
    return posts


def get_sorted_subscriptions_posts(user_id: int):
    subscriptions = get_subscriptions(user_id)
    posts = []
    for user in subscriptions:
        user_posts = requests.get(f"{HOST.URL}/posts/{user['id']}/all").json()
        posts.extend(user_posts)
    posts = sort_posts(posts)
    return posts


def get_sorted_other_posts(user_id: int):
    subscriptions = get_subscriptions(user_id)
    all_users = get_users()
    me = get_user(user_id)
    all_users.remove(me)
    for user in subscriptions:
        all_users.remove(user)
    posts = []
    for user in all_users:
        user_posts = requests.get(f"{HOST.URL}/posts/{user['id']}/all").json()
        posts.extend(user_posts)
    posts = sort_posts(posts)
    return posts
