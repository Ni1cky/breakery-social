import datetime
import random

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.recycleview import RecycleView
from kivymd.uix.list import MDList
import current_user
from store.models.models import Message
from views.base import BaseScreen
from views.meta import SCREENS
from components.message.message import MessageWidget
from controllers.message import get_time_send_sorted_message

Builder.load_file('views/dialog_screen/dialog_screen.kv')


class DialogScreen(BaseScreen):
    SCREEN_NAME = SCREENS.DIALOG_SCREEN
    scrollable_messages: RecycleView = ObjectProperty()
    messages: MDList = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scrollable_messages.data = []

        for i in range(1, 40):
            print(len(i * "привет") // 20 * 100)
            self.scrollable_messages.data.append({'message_text': i * "привет)",
                                                        'time_send': datetime.datetime(2019, 6, 1, 12, 22),
                                                        'is_read': False,
                                                        'is_important': False,
                                                        'is_edited': False,
                                                  "height": int(max(len(i * "привет") / 40, 1) * 50),
                                                'send_from_me': i % 2})

    def get_validate_message(self, recipient_id):
        messages = get_time_send_sorted_message(current_user.CURRENT_USER_ID, recipient_id)
        # for message in messages:
        #     if message.id == recipient_id:
        #         message.send_from_me = True
        #     else:
        #         message.send_from_me = False
        return messages

    def reload_messages(self):
        messages = self.get_validate_message(2)
        self.messages.clear_widgets()
        for message in messages:
            message: Message
            self.messages.add_widget(MessageWidget(message))
