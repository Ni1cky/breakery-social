import requests
import os
from base64 import b64decode, b64encode

from controllers.authorization import send
from views.meta import HOST

FOLDER_WITH_PHOTOS = "photos"


def create_path(user_id: int):
    if not os.path.exists(FOLDER_WITH_PHOTOS):
        os.mkdir(FOLDER_WITH_PHOTOS)
    if not os.path.exists(f"{FOLDER_WITH_PHOTOS}/{user_id}"):
        os.mkdir(f"{FOLDER_WITH_PHOTOS}/{user_id}")


def get_path_to_user_profile_image(user_id: int):
    return f"{FOLDER_WITH_PHOTOS}/{user_id}/profile"


def encode_image(path_to_image: str):
    img = open(path_to_image, "rb").read()
    enc_img = b64encode(img).decode()
    return enc_img


def decode_image(enc_img: str):
    dec_img = b64decode(enc_img.encode())
    return dec_img


def set_user_profile_picture(user_id: int, path_to_image: str):
    enc_img = encode_image(path_to_image)
    req = requests.Request('PUT', f"{HOST.URL}/photos/{user_id}/profile",json={"source": enc_img})
    response = send(req)
    #requests.put(f"{HOST.URL}/photos/{user_id}/profile",json={"source": enc_img})
    create_path(user_id)
    img = open(path_to_image, "rb").read()
    open(f"{FOLDER_WITH_PHOTOS}/{user_id}/profile", "wb").write(img)


def refresh_user_profile_picture(user_id: int):
    req = requests.Request('GET', f"{HOST.URL}/photos/{user_id}/profile")
    enc_img = send(req).json()
    #enc_img = requests.get(f"{HOST.URL}/photos/{user_id}/profile").json()
    img = decode_image(enc_img)
    create_path(user_id)
    open(f"{FOLDER_WITH_PHOTOS}/{user_id}/profile", "wb").write(img)


def set_default_picture(login: str):
    enc_img = encode_image('img/profile.jpg')
    req = requests.Request('POST', f"{HOST.URL}/photos/default", json={"source": enc_img}, params={"login": login})
    resp = send(req)
    #requests.post(f"{HOST.URL}/photos/default", json={"source": enc_img}, params={"login": login})


def get_path_to_user_post(user_id: int, post_id: int):
    return f"{FOLDER_WITH_PHOTOS}/{user_id}/{post_id}"


def add_post_picture(user_id: int, post_id: int, path_to_image: str):
    enc_img = '' if not path_to_image else encode_image(path_to_image)
    req = requests.Request('POST', f"{HOST.URL}/photos/{user_id}/{post_id}", json={'source': enc_img})
    resp = send(req)
    #requests.post(f"{HOST.URL}/photos/{user_id}/{post_id}", json={'source': enc_img})


def get_post_picture(user_id: int, post_id: int):
    req = requests.Request('GET', F"{HOST.URL}/photos/{user_id}/{post_id}")
    enc_img = send(req).json()
    #enc_img = requests.get(F"{HOST.URL}/photos/{user_id}/{post_id}").json()
    img = decode_image(enc_img)
    open(f"{FOLDER_WITH_PHOTOS}/{user_id}/{post_id}", 'wb').write(img)
    return f"{FOLDER_WITH_PHOTOS}/{user_id}/{post_id}" if img else ''
