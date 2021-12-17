from kivy.uix.screenmanager import ScreenManager
from views.message_screen.message_screen import MessageScreen


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MessageScreen())
        self.current = MessageScreen.SCREEN_NAME

