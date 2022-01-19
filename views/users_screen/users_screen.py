from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineAvatarListItem, ImageLeftWidget
import requests

from views.base import BaseScreen
from views import meta

Builder.load_file('views/users_screen/users_screen.kv')


class UsersScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.USERS_SCREEN
    users_list = ObjectProperty()

    def on_enter(self, *args):
        self.users_list.clear_widgets()
        all_users = requests.get("http://127.0.0.1:8000/users")
        for user in all_users.json():
            item = OneLineAvatarListItem(text=f"{user['name']} {user['surname']}")
            item.add_widget(ImageLeftWidget(source=user['photo']))
            self.users_list.add_widget(item)
