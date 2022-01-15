from kivy.uix.screenmanager import ScreenManager
from views.authorization.authorization import LoginScreen
from views.dialog_screen.dialog_screen import DialogScreen
from views.message_screen.message_screen import MessageScreen
from views.news_screen.news_screen import NewsScreen
from views.profile_screen.profile_screen import ProfileScreen


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MessageScreen())
        self.add_widget(ProfileScreen())
        self.add_widget(NewsScreen())
        self.add_widget(DialogScreen())
        self.add_widget(LoginScreen())
        self.current = LoginScreen.SCREEN_NAME
