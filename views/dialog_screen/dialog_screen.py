import datetime
import requests
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView
from kivymd.uix.textfield import MDTextField

from controllers.authorization import get_my_profile
from controllers.dialogs import get_dialog
from controllers.user import get_current_user
from store.models.models import Message, MessageCreate
from views.base import BaseScreen
from views.meta import SCREENS
from controllers.message import get_time_send_sorted_message, create_message

Builder.load_file('views/dialog_screen/dialog_screen.kv')


class DialogScreen(BaseScreen):
    SCREEN_NAME = SCREENS.DIALOG_SCREEN
    scrollable_messages: RecycleView = ObjectProperty()
    message_text: MDTextField = ObjectProperty()

    def __init__(self, id=1, **kwargs):
        super().__init__(**kwargs)
        self.scrollable_messages.data = []
        # self.data = get_dialog(id)

    def get_validate_message(self, recipient_id):
        current_user = get_current_user()
        messages = get_time_send_sorted_message(current_user.id, recipient_id)
        for message in messages:
            if message.sender_id == get_current_user().id:
                message.send_from_me = True
            else:
                message.send_from_me = False
        return messages

    def reload_messages(self):
        # messages = self.get_validate_message(2)
        messages = []
        self.scrollable_messages.data = []
        for message in messages:
            message: Message
            data = message.dict()
            data["message_text"] = data.pop("text")
            # if data["id"] == current_user.CURRENT_USER_ID:
            #     data["send_from_me"] = 1
            # else:
            #     data["send_from_me"] = 0
            self.scrollable_messages.data.append(data)

    def send_message(self):
        current_user = get_current_user()
        message = MessageCreate(text=self.message_text.text, time_send=datetime.datetime.now(), sender_id=current_user.id, dialog_id=self.data.id)
        create_message(message)
