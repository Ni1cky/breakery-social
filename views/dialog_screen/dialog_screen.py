from kivy.lang import Builder
from kivy.properties import ObjectProperty
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
    scrollable_messages = ObjectProperty()
    messages: MDList = ObjectProperty()

    def get_validate_message(self, recipient_id):
        messages = get_time_send_sorted_message(current_user.CURRENT_USER_ID, recipient_id)
        for message in messages:
            if message.id == recipient_id:
                message.send_from_me = True
            else:
                message.send_from_me = False
        return messages
    
    def reload_messages(self):
        messages = self.get_validate_message(2)
        for message in messages:
            message: Message
            self.messages.add_widget(MessageWidget(message))
