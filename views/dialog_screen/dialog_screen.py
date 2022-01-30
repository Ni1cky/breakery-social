import datetime
import requests
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView
from kivymd.uix.textfield import MDTextField
from controllers.authorization import get_my_profile
from store.models.models import Message, MessageCreate
from kivymd.uix.list import TwoLineAvatarIconListItem

from controllers.authorization import get_my_profile
from controllers.dialog import get_dialog_by_id
from controllers.user import get_user
from store.models.models import Message
from views.base import BaseScreen
from views.meta import SCREENS
from controllers.message import get_time_send_sorted_message, create_message

Builder.load_file('views/dialog_screen/dialog_screen.kv')


class DialogScreen(BaseScreen):
    SCREEN_NAME = SCREENS.DIALOG_SCREEN
    scrollable_messages: RecycleView = ObjectProperty()
    header: TwoLineAvatarIconListItem = ObjectProperty()
    message_text: MDTextField = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog_data = None

        # for i in range(1, 40):
        #     print(len(i * "привет") // 20 * 100)
        #     self.scrollable_messages.data.append({'message_text': i * "привет)",
        #                                                 'time_send': datetime.datetime(2019, 6, 1, 12, 22),
        #                                                 'is_read': False,
        #                                                 'is_important': False,
        #                                                 'is_edited': False,
        #                                           "height": int(max(len(i * "привет") / 40, 1) * 50),
        #                                         'send_from_me': i % 2})

    def get_validate_message(self, recipient_id):
        messages = get_time_send_sorted_message(get_my_profile()["id"], recipient_id)
        for message in messages:
            if message.id == recipient_id:
                message.send_from_me = True
            else:
                message.send_from_me = False
        return messages

    def reload_messages(self):
        messages = self.get_validate_message(self.dialog_data["another_user_id"])
        self.scrollable_messages.data = []
        for message in messages:
            message: Message
            data = message.dict()
            data["message_text"] = data.pop("text")
            if data["id"] == get_my_profile()["id"]:
                data["send_from_me"] = 1
            else:
                data["send_from_me"] = 0
            self.scrollable_messages.data.append(data)

    def send_message(self):
        current_user = get_my_profile()
        message = MessageCreate(text=self.message_text.text, time_send=datetime.datetime.now(), sender_id=current_user["id"], dialog_id=self.dialog_data["dialog_id"])
        create_message(message)

    def load_dialog(self, dialog_id: int):
        self.dialog_data = None
        dialog = get_dialog_by_id(dialog_id)
        if dialog.user1_id == get_my_profile()["id"]:
            self.dialog_data = {"current_user_id": dialog.user1_id, "another_user_id": dialog.user2_id}
            another_user = get_user(dialog.user2_id)
            self.header.text = f"{another_user['name']} {another_user['surname']}"
        else:
            self.dialog_data = {"current_user_id": dialog.user2_id, "another_user_id": dialog.user1_id}
            another_user = get_user(dialog.user1_id)
            self.header.text = f"{another_user['name']} {another_user['surname']}"
        self.dialog_data["dialog_id"] = dialog.id
