import datetime
import requests

from controllers.authorization import send
from views.meta import HOST
from controllers.photo import add_post_picture
from controllers.subscription import get_subscriptions
from controllers.user import get_users, get_user

DATE_FORMAT = "%d %b %y  %H:%M"
POSTS_BLOCK_SIZE = 50


def add_post(user_id: int, text: str, time_created: str, path_to_image: str):
    req = requests.Request('POST', f"{HOST.URL}/newpost", json={'author_id': user_id, 'text': text, 'time_created': time_created})
    r = send(req)
    #r = requests.post(f"{HOST.URL}/newpost", json={'author_id': user_id, 'text': text, 'time_created': time_created})
    post_id = r.json()
    add_post_picture(user_id, post_id, path_to_image)


def get_post_by_id(post_id: int):
    req = requests.Request('GET', f"{HOST.URL}/posts/{post_id}")
    post = send(req).json()
    #post = requests.get(f"{HOST.URL}/posts/{post_id}").json()
    return post


def sort_posts(posts: list):
    return sorted(posts, key=lambda x: x['id'], reverse=True)


def get_sorted_user_posts(user_id: int):
    req = requests.Request('GET', f"{HOST.URL}/posts/{user_id}/all")
    posts = send(req).json()
    #posts = requests.get(f"{HOST.URL}/posts/{user_id}/all").json()
    posts = sort_posts(posts)
    return posts


def get_last_post_id():
    req = requests.Request('GET', f"{HOST.URL}/posts_last_id")
    post_id = send(req).json()
    #post_id = requests.get(f"{HOST.URL}/posts_last_id").json()
    return post_id


def get_block_of_all_posts(max_id: int):
    min_id = max_id - POSTS_BLOCK_SIZE
    req = requests.Request('GET', f"{HOST.URL}/posts", params={"min_id": min_id, "max_id": max_id})
    block = send(req).json()
    #block = requests.get(f"{HOST.URL}/posts", params={"min_id": min_id, "max_id": max_id}).json()
    return block


def get_all_sorted_posts(user_id):
    req = requests.Request('GET', f"{HOST.URL}/posts")
    posts = send(req).json()
    #posts = requests.get(f"{HOST.URL}/posts").json()

    #subscriptions = requests.get(f"{HOST.URL}/subscriptions/{user_id}/subscriptions").json()
    req = requests.Request('GET', f"{HOST.URL}/subscriptions/{user_id}/subscriptions")
    subscriptions = send(req).json()

    subscriptions_ids = [s['user_id'] for s in subscriptions]
    posts.sort(key=lambda x: (x['author_id'] in subscriptions_ids, x['id']), reverse=True)
    return posts


def get_sorted_subscriptions_posts(user_id: int):
    subscriptions = get_subscriptions(user_id)
    posts = []
    for user in subscriptions:
        req = requests.Request('GET', f"{HOST.URL}/posts/{user['id']}/all")
        user_posts = send(req).json()
        #user_posts = requests.get(f"{HOST.URL}/posts/{user['id']}/all").json()
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
        req = requests.Request('GET', f"{HOST.URL}/posts/{user['id']}/all")
        user_posts = send(req).json()
        #user_posts = requests.get(f"{HOST.URL}/posts/{user['id']}/all").json()
        posts.extend(user_posts)
    posts = sort_posts(posts)
    return posts
