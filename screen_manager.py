from kivy.uix.screenmanager import ScreenManager
from main_menu.menu import MainMenuScreen
from views.authorization.authorization import LoginScreen
from views.dialog_screen.dialog_screen import DialogScreen
from views.message_screen.message_screen import MessageScreen
from views.profile_screen.profile_screen import ProfileScreen


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MessageScreen())
        self.add_widget(ProfileScreen())
        self.add_widget(DialogScreen())
        self.current = ProfileScreen.SCREEN_NAME


class MainManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(LoginScreen())
        self.add_widget(MainMenuScreen())
        self.current = LoginScreen.SCREEN_NAME
