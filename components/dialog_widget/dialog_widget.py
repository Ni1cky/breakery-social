from kivy.lang import Builder
from kivymd.uix.list import TwoLineAvatarIconListItem
from store.models.models import Message

Builder.load_file('components/dialog_widget/dialog_widget.kv')


class DialogWidget(TwoLineAvatarIconListItem):
    def __init__(self, message: Message, name="user", last_message="кинуть физику)", **kwargs):
        super().__init__(text=name, secondary_text=last_message, **kwargs)
        self.data = message
        self.name = name
        self.last_message = last_message
