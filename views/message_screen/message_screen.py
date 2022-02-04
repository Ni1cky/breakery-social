from kivy.properties import ObjectProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from controllers.authorization import get_my_profile
from controllers.dialog import get_users_dialogs
from views.base import BaseScreen
from views.meta import SCREENS
from kivy.lang import Builder

Builder.load_file('views/message_screen/message_screen.kv')


class MessageScreen(BaseScreen):
    SCREEN_NAME = SCREENS.MESSAGE_SCREEN
    dialogs_list: RecycleBoxLayout = ObjectProperty()
    dialogs_recycle_view: RecycleView = ObjectProperty()

    def on_enter(self, *args):
        get_users_dialogs(get_my_profile()["id"])
