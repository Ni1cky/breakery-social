from kivy.lang import Builder
from kivy.properties import ObjectProperty

from controllers.authorization import get_my_profile
from controllers.subscription import get_subscriptions, get_subscribers
from components.user_list_item.user_list_item import UserListItem
from views.base import BaseScreen
from views import meta

Builder.load_file('views/subscribers_screen/subscribers_screen.kv')


class SubscribersScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.SUBSCRIBERS_SCREEN
    subscribers_list = ObjectProperty()

    def on_enter(self, *args):
        self.subscribers_list.clear_widgets()
        me = get_my_profile()
        subscribers = get_subscribers(me["id"])
        my_subscriptions = get_subscriptions(me["id"])
        for user in subscribers:
            self.subscribers_list.add_widget(UserListItem(user, True if user in my_subscriptions else False))
