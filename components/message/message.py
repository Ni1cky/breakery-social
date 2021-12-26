from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivymd.uix.list import OneLineListItem
from store.models.models import Message
from kivy.lang import Builder

Builder.load_file('components/message/message.kv')


class MessageWidget(OneLineListItem):
    message_text = StringProperty()
    message = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # .message_text = message["text"]
