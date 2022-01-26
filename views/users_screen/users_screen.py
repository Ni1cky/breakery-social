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

    def on_enter(self, *args):
        self.users_list.clear_widgets()
        all_users = get_users()
        my_subscriptions = get_subscriptions(get_my_profile()["id"])
        for user in all_users:
            item = UserListItem(user, True if user in my_subscriptions else False)
            self.users_list.add_widget(item)
