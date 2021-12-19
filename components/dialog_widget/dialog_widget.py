from kivy.uix.widget import Widget
from kivymd.uix.list import OneLineListItem, TwoLineAvatarListItem, TwoLineAvatarIconListItem

from components.message.message import MessageWidget
from store.models.models import Message
from kivy.lang import Builder

Builder.load_file('components/dialog_widget/dialog_widget.kv')


class DialogWidget(TwoLineAvatarIconListItem):
    def __init__(self, message: Message, name="user", last_message="кинуть физику)", **kwargs):
        super().__init__(text=name, secondary_text=last_message, **kwargs)
        self.data = message
        self.name = name
        self.last_message = last_message
