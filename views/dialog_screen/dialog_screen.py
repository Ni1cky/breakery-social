import datetime
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.list import MDList
from components.dialog_widget.dialog_widget import DialogWidget
from views.base import BaseScreen
from views.meta import SCREENS
from components.message.message import MessageWidget
from controllers.message import get_time_send_sorted_message


Builder.load_file('views/dialog_screen/dialog_screen.kv')


class DialogScreen(BaseScreen):
    SCREEN_NAME = SCREENS.DIALOG_SCREEN
    scrollable_messages = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        list_view = MDList()
        for _ in range(13):
            '''tmp_message = MessageWidget(message={'text': 'sdasd',
    'time_send': datetime.datetime.now(),
    'is_read': False,
    'is_important': False,
    'is_edited': False})
            
            list_view.add_widget(MessageWidget(tmp_message))'''
            list_view.add_widget(MessageWidget(message={'text': 'dsdssd',
                                                       'time_send': datetime.datetime(2019, 6, 1, 12, 22),
                                                       'is_read': False,
                                                       'is_important': False,
                                                       'is_edited': False}))
        self.scrollable_messages.add_widget(list_view)


    def get_validate_message(sender_id: int, recipient_id: int):
        #messages = get_time_send_sorted_message(sender_id, recipient_id)
        messages = []
        for message in messages:
            if message.id == recipient_id:
                message.send_from_me = True
            else:
                message.send_from_me = False
        return messages
