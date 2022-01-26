from kivy.lang import Builder
from kivy.properties import ObjectProperty

from controllers.authorization import get_my_profile
from controllers.subscription import get_subscriptions
from views.base import BaseScreen
from views import meta
from components.user_list_item.user_list_item import UserListItem

Builder.load_file('views/subscriptions_screen/subscriptions_screen.kv')


class SubscriptionsScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.SUBSCRIPTIONS_SCREEN
    subscriptions_list = ObjectProperty()

    def on_enter(self, *args):
        self.subscriptions_list.clear_widgets()
        me = get_my_profile()
        subscriptions = get_subscriptions(me["id"])
        for user in subscriptions:
            self.subscriptions_list.add_widget(UserListItem(user, True))
