from kivy.properties import ObjectProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from views.base import BaseScreen
from views.meta import SCREENS
from kivy.lang import Builder

Builder.load_file('views/message_screen/message_screen.kv')


class MessageScreen(BaseScreen):
    SCREEN_NAME = SCREENS.MESSAGE_SCREEN
    dialogs_list: RecycleBoxLayout = ObjectProperty()
    dialogs_recycle_view: RecycleView = ObjectProperty()
