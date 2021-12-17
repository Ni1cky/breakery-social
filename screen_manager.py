from kivy.uix.screenmanager import ScreenManager
from main_menu.menu import MainMenuScreen
from views.authorization.authorization import LoginScreen
from views.message_screen.message_screen import MessageScreen


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MessageScreen())
        self.current = MessageScreen.SCREEN_NAME


class MainManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(LoginScreen())
        self.add_widget(MainMenuScreen())
        self.current = LoginScreen.SCREEN_NAME
