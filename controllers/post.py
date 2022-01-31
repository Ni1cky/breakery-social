import datetime
import requests

from views.meta import HOST
from controllers.photo import add_post_picture


DATE_FORMAT = "%d %b %y  %H:%M"


def add_post(user_id: int, text: str, time_created: str, path_to_image: str):
    r = requests.post(f"{HOST.URL}/newpost", json={'author_id': user_id, 'text': text, 'time_created': time_created})
    post_id = r.json()
    add_post_picture(user_id, post_id, path_to_image)


def get_time_sorted_posts(user_id: int):
    posts = requests.get(f"{HOST.URL}/posts/{user_id}/all").json()
    posts.sort(key=lambda x: datetime.datetime.strptime(x['time_created'], DATE_FORMAT), reverse=True)
    return posts
