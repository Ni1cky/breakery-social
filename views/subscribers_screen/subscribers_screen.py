from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineAvatarListItem, ImageLeftWidget
import requests
from controllers.authorization import get_my_profile
from views.base import BaseScreen
from views import meta
from views.meta import HOST

Builder.load_file('views/subscribers_screen/subscribers_screen.kv')


class SubscribersScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.SUBSCRIBERS_SCREEN
    subscribers_list = ObjectProperty()

    def on_enter(self, *args):
        self.subscribers_list.clear_widgets()
        me = get_my_profile()
        subscribers = requests.get(f"{HOST.URL}/subscriptions/{me['id']}/subscribers").json()
        for data in subscribers:
            user = requests.get(f"{HOST.URL}/users/{data['subscriber_id']}").json()
            item = OneLineAvatarListItem(text=f"{user['name']} {user['surname']}")
            item.add_widget(ImageLeftWidget(source=user['photo']))
            self.subscribers_list.add_widget(item)
