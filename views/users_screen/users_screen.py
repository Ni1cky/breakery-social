from math import ceil
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from components.user_list_item.user_list_item import UserListItem
from controllers.user import get_users, get_block_of_all_users, USERS_BLOCK_SIZE
from controllers.subscription import get_subscriptions_ids
from controllers.authorization import get_my_profile
from views.base import BaseScreen
from views import meta

Builder.load_file('views/users_screen/users_screen.kv')


class UsersScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.USERS_SCREEN
    users_list = ObjectProperty()
    sv = ObjectProperty()
    ON_SCREEN = 10
    delta = 0
    min_y = 1
    loaded = 0
    all_users_loaded = False
    subscriptions_ids = []
    me = {}
    search_id = 0

    def on_enter(self, *args):
        self.users_list.clear_widgets()
        self.me = get_my_profile()
        self.sv.scroll_y = 1
        self.subscriptions_ids = get_subscriptions_ids(self.me["id"])
        self.all_users_loaded = False
        self.search_id = 0
        self.load_block()
        self.min_y = 1
        self.loaded = 0
        for i in range(1, min(self.ON_SCREEN, len(self.users_list.children)) + 1):
            self.users_list.children[-i].load_image()
            self.loaded += 1

    def update_screen(self):
        y = self.sv.scroll_y
        if y < self.min_y:
            if not self.all_users_loaded and len(self.users_list.children) - self.loaded < 4:
                self.load_block()
                y = self.sv.scroll_y

            self.min_y = y
            cnt = ceil((1 - y) / self.delta) + 10

            for i in range(self.loaded, min(len(self.users_list.children), cnt + 1)):
                self.users_list.children[-(i + 1)].load_image()
                self.loaded += 1

    def load_block(self):
        block = get_block_of_all_users(self.search_id)
        self.search_id += USERS_BLOCK_SIZE

        if not block:
            self.all_users_loaded = True
            return

        for user in block:
            if user != self.me:
                item = UserListItem(user, True if user['id'] in self.subscriptions_ids else False)
                self.users_list.add_widget(item)

        self.delta = 1 / len(self.users_list.children) if len(self.users_list.children) else 1
