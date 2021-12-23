from kivymd.uix.list import MDList
from kivy.uix.scrollview import ScrollView
from views.base import BaseScreen
from views.meta import SCREENS
from kivy.lang import Builder
import datetime
from components.dialog_widget.dialog_widget import DialogWidget
from controllers.message import get_time_send_sorted_message
from store.models.models import Message

Builder.load_file('views/message_screen/message_screen.kv')


class MessageScreen(BaseScreen):
    SCREEN_NAME = SCREENS.MESSAGE_SCREEN

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scroll = ScrollView()
        list_view = MDList()
        for _ in range(13):
            list_view.add_widget(DialogWidget(message=Message(text='dsdssd',
                                                              time_send=datetime.datetime(2019, 6, 1, 12, 22),
                                                              is_read=False,
                                                              is_important=False,
                                                              is_edited=False), name="User"))
        self.add_widget(MDList())
        scroll.add_widget(list_view)
        self.add_widget(scroll)

    def get_validate_message(sender_id: int, recipient_id: int):
        messages = get_time_send_sorted_message(sender_id, recipient_id)
        for message in messages:
            if message.id == recipient_id:
                message.send_from_me = True
            else:
                message.send_from_me = False
        return messages
