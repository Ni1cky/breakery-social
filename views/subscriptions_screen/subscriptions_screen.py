from kivy.lang import Builder
from kivy.properties import ObjectProperty
from math import ceil

from controllers.authorization import get_my_profile
from controllers.subscription import get_subscriptions
from views.base import BaseScreen
from views import meta
from components.user_list_item.user_list_item import UserListItem

Builder.load_file('views/subscriptions_screen/subscriptions_screen.kv')


class SubscriptionsScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.SUBSCRIPTIONS_SCREEN
    users_list = ObjectProperty()
    sv = ObjectProperty()
    ON_SCREEN = 10
    delta = 0
    min_y = 1
    loaded = 0
    users_to_load = []

    def on_enter(self, *args):
        self.users_list.clear_widgets()
        me = get_my_profile()
        self.users_to_load = get_subscriptions(me["id"])
        for user in self.users_to_load:
            self.users_list.add_widget(UserListItem(user, True))
        self.delta = 1 / len(self.users_list.children) if len(self.users_list.children) else 1
        self.min_y = 1
        self.loaded = 0
        for i in range(1, min(self.ON_SCREEN, len(self.users_to_load)) + 1):
            self.users_list.children[-i].load_image()
            self.loaded += 1

    def update_screen(self):
        y = self.sv.scroll_y
        if y < self.min_y:
            self.min_y = y
            cnt = ceil((1 - y) / self.delta) + 10
            for i in range(self.loaded, min(len(self.users_to_load), cnt + 1)):
                self.users_list.children[-(i + 1)].load_image()
                self.loaded += 1
