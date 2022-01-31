import requests
import os
from base64 import b64decode, b64encode

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


def get_user_images(user_id: int):
    response = requests.get(f"{HOST.URL}/photos/{user_id}").json()
    for photo in response:
        dec_photo = decode_image(photo["source"])
        post_id = photo["post_id"]
        create_path(user_id)
        path_to_dir = f"{FOLDER_WITH_PHOTOS}/{user_id}"
        if post_id is None:
            open(f"{path_to_dir}/profile", "wb").write(dec_photo)
        else:
            open(f"{path_to_dir}/{post_id}", "wb").write(dec_photo)


def set_user_profile_picture(user_id: int, path_to_image: str):
    enc_img = encode_image(path_to_image)
    requests.put(f"{HOST.URL}/photos/{user_id}/profile",json={"source": enc_img})
    create_path(user_id)
    img = open(path_to_image, "rb").read()
    open(f"{FOLDER_WITH_PHOTOS}/{user_id}/profile", "wb").write(img)


def refresh_user_profile_picture(user_id: int):
    enc_img = requests.get(f"{HOST.URL}/photos/{user_id}/profile").json()
    img = decode_image(enc_img)
    create_path(user_id)
    open(f"{FOLDER_WITH_PHOTOS}/{user_id}/profile", "wb").write(img)


def set_default_picture(login: str):
    enc_img = encode_image('img/profile.jpg')
    requests.post(f"{HOST.URL}/photos/default", json={"source": enc_img}, params={"login": login})