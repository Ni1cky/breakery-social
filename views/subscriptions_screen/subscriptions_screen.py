from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineAvatarListItem, ImageLeftWidget
import requests

from controllers.authorization import get_my_profile
from views.base import BaseScreen
from views import meta

Builder.load_file('views/subscriptions_screen/subscriptions_screen.kv')


class SubscriptionsScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.SUBSCRIPTIONS_SCREEN
    subscriptions_list = ObjectProperty()

    def on_enter(self, *args):
        self.subscriptions_list.clear_widgets()
        me = get_my_profile()
        subscribers = requests.get(f"http://127.0.0.1:8000/subscriptions/{me['id']}/subscriptions").json()
        for data in subscribers:
            user = requests.get(f"http://127.0.0.1:8000/users/{data['user_id']}").json()
            item = OneLineAvatarListItem(text=f"{user['name']} {user['surname']}")
            item.add_widget(ImageLeftWidget(source=user['photo']))
            self.subscriptions_list.add_widget(item)
