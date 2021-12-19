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

Builder.load_file('views/dialog_screen/dialog_screen.kv')

class DialogScreen(BaseScreen):
    SCREEN_NAME = SCREENS.DIALOG_SCREEN
    scrollable_messages = ObjectProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scrollable_messages = ScrollView()
        list_view = MDList()
        for _ in range(13):
            '''tmp_message = MessageWidget(message={'text': 'sdasd',
    'time_send': datetime.datetime.now(),
    'is_read': False,
    'is_important': False,
    'is_edited': False})
            
            list_view.add_widget(MessageWidget(tmp_message))'''
            list_view.add_widget(DialogWidget(message={'text': 'dsdssd',
                                                       'time_send': datetime.datetime(2019, 6, 1, 12, 22),
                                                       'is_read': False,
                                                       'is_important': False,
                                                       'is_edited': False}, name="User"))
        self.add_widget(MDList())
        scrollable_messages.add_widget(list_view)
        self.add_widget(scrollable_messages)
