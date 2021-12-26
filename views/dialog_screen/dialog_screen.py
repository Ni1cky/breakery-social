import datetime
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.list import MDList

import social
from components.dialog_widget.dialog_widget import DialogWidget
from store.models.models import Message
from views.base import BaseScreen
from views.meta import SCREENS
from components.message.message import MessageWidget
from controllers.message import get_time_send_sorted_message

Builder.load_file('views/dialog_screen/dialog_screen.kv')


class DialogScreen(BaseScreen):
    SCREEN_NAME = SCREENS.DIALOG_SCREEN
    scrollable_messages = ObjectProperty()
    messages: MDList = ObjectProperty()

    def __init__(self, another_persons_id: int, **kwargs):
        super().__init__(**kwargs)
        self.another_persons_id = another_persons_id

    def get_validate_message(self):
        messages = get_time_send_sorted_message(social.SocialApp.current_user_id, self.another_persons_id)
        # messages = []
        for message in messages:
            if message.id == self.another_persons_id:
                message.send_from_me = True
            else:
                message.send_from_me = False
        return messages
    
    def reload_messages(self):
        messages = self.get_validate_message()
        for message in messages:
            message: Message
            self.messages.add_widget(MessageWidget(message))
