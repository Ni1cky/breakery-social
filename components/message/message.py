from kivy.uix.widget import Widget
from store.models.models import Message
from kivy.lang import Builder

Builder.load_file('components/message/message.kv')


class MessageWidget(Widget):
    def __init__(self, message: Message, **kwargs):
        super().__init__(**kwargs)
        self.data = message
