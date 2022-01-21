from kivy.uix.screenmanager import ScreenManager
from views import meta
from views.authorization.authorization import LoginScreen
from views.authorization.registration import RegisterScreen
from views.dialog_screen.dialog_screen import DialogScreen
from views.message_screen.message_screen import MessageScreen
from views.meta import AUTHORIZATION
from views.news_screen.news_screen import NewsScreen
from views.profile_screen.profile_screen import ProfileScreen
from views.users_screen.users_screen import UsersScreen


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MessageScreen())
        self.add_widget(ProfileScreen())
        self.add_widget(NewsScreen())
        self.add_widget(DialogScreen())
        self.add_widget(LoginScreen())
        self.add_widget(RegisterScreen())
        self.add_widget(UsersScreen())
        try:
            f = open('saved\\access_token', 'r').read()
            AUTHORIZATION.TOKEN = str(f)
            self.current = meta.SCREENS.PROFILE_SCREEN
        except:
            self.current = LoginScreen.SCREEN_NAME

