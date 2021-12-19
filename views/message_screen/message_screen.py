from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem, MDList
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from views.base import BaseScreen
from views.meta import SCREENS
from kivy.lang import Builder
from components.message.message import MessageWidget
import datetime
from components.dialog_widget.dialog_widget import DialogWidget

Builder.load_file('views/message_screen/message_screen.kv')

class MessageScreen(BaseScreen):
    SCREEN_NAME = SCREENS.MESSAGE_SCREEN


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scroll = ScrollView()
        list_view = MDList()
        for _ in range(13):
            list_view.add_widget(DialogWidget(message={'text': 'dsdssd',
                                                                    'time_send': datetime.datetime(2019, 6, 1, 12, 22),
                                                                    'is_read': False,
                                                                    'is_important': False,
                                                                    'is_edited': False}, name="User"))
        self.add_widget(MDList())
        scroll.add_widget(list_view)
        self.add_widget(scroll)
