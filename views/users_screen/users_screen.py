from kivy.lang import Builder
from kivy.properties import ObjectProperty
import requests

from views.base import BaseScreen
from views import meta

Builder.load_file('views/users_screen/users_screen.kv')


class UsersScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.USERS_SCREEN
    users_list = ObjectProperty()

    def __init__(self, **kwargs):
        super(UsersScreen, self).__init__(**kwargs)
        req = requests.get("http://127.0.0.1:8000/users").json()
        print(req)
