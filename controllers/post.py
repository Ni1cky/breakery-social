import requests

from views.meta import HOST
from controllers.photo import add_post_picture


def add_post(user_id: int, text: str, time_created: str, path_to_image: str):
    r = requests.post(f"{HOST.URL}/newpost", json={'author_id': user_id, 'text': text, 'time_created': time_created})
    post_id = r.json()
    add_post_picture(user_id, post_id, path_to_image)
