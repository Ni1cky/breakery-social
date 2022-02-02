from kivy.lang import Builder
from kivy.properties import ObjectProperty
from math import ceil

from controllers.authorization import get_my_profile
from controllers.subscription import get_subscriptions_ids, get_subscribers_ids
from controllers.user import USERS_BLOCK_SIZE, get_user
from components.user_list_item.user_list_item import UserListItem
from views.base import BaseScreen
from views import meta

Builder.load_file('views/subscribers_screen/subscribers_screen.kv')


class SubscribersScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.SUBSCRIBERS_SCREEN
    users_list = ObjectProperty()
    sv = ObjectProperty()
    ON_SCREEN = 10
    delta = 0
    min_y = 1
    loaded = 0
    users_to_load = []
    subscriptions_ids = []

    def on_enter(self, *args):
        self.users_list.clear_widgets()
        me = get_my_profile()
        self.users_to_load = get_subscribers_ids(me["id"])
        self.subscriptions_ids = get_subscriptions_ids(me["id"])
        self.load_block()
        self.min_y = 1
        self.loaded = 0
        for i in range(1, min(self.ON_SCREEN, len(self.users_to_load)) + 1):
            self.users_list.children[-i].load_image()
            self.loaded += 1

    def update_screen(self):
        y = self.sv.scroll_y
        if y < self.min_y:
            if len(self.users_list.children) - self.loaded < 4:
                self.load_block()
                y = self.sv.scroll_y

            self.min_y = y
            cnt = ceil((1 - y) / self.delta) + 10

            for i in range(self.loaded, min(len(self.users_to_load), cnt + 1)):
                self.users_list.children[-(i + 1)].load_image()
                self.loaded += 1

    def load_block(self):
        block = self.users_to_load[len(self.users_list.children):len(self.users_list.children) + USERS_BLOCK_SIZE]

        if not block:
            return

        for user_id in block:
            user = get_user(user_id)
            self.users_list.add_widget(UserListItem(user, True if user_id in self.subscriptions_ids else False))

        self.delta = 1 / len(self.users_list.children) if len(self.users_list.children) else 1
