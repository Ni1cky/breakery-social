from math import ceil
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from components.user_list_item.user_list_item import UserListItem
from controllers.user import get_users
from controllers.subscription import get_subscriptions
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
    users_to_load = []

    def on_enter(self, *args):
        self.users_list.clear_widgets()
        self.users_to_load = get_users()
        me = get_my_profile()
        my_subscriptions = get_subscriptions(me["id"])
        self.users_to_load.remove(me)
        for user in self.users_to_load:
            item = UserListItem(user, True if user in my_subscriptions else False)
            self.users_list.add_widget(item)
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
