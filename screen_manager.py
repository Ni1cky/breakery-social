from kivy.uix.screenmanager import ScreenManager
from views import meta
from views.add_new_news_screen.add_new_news_screen import AddNewNewsScreen
from views.authorization.authorization import LoginScreen
from views.authorization.registration import RegisterScreen
from views.dialog_screen.dialog_screen import DialogScreen
from views.message_screen.message_screen import MessageScreen
from views.meta import AUTHORIZATION
from views.news_screen.news_screen import NewsScreen
from views.people_screen.people_screen import PeopleScreen
from views.profile_screen.profile_screen import ProfileScreen
from views.users_screen.users_screen import UsersScreen
from views.my_news_screen.my_news_screen import MyNewsScreen
from views.subscribers_screen.subscribers_screen import SubscribersScreen
from views.subscriptions_screen.subscriptions_screen import SubscriptionsScreen
from views.likes_screen.likes_screen import LikesScreen
from controllers.authorization import get_my_profile

class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MessageScreen())
        self.add_widget(MyNewsScreen())
        self.add_widget(ProfileScreen())
        self.add_widget(NewsScreen())
        self.add_widget(DialogScreen())
        self.add_widget(LoginScreen())
        self.add_widget(RegisterScreen())
        self.add_widget(UsersScreen())
        self.add_widget(PeopleScreen())
        self.add_widget(SubscribersScreen())
        self.add_widget(SubscriptionsScreen())
        self.add_widget(AddNewNewsScreen())
        self.add_widget(LikesScreen())
        try:
            f = open('saved\\access_token', 'r').read()
            AUTHORIZATION.TOKEN = str(f)
            get_my_profile()
            self.current = meta.SCREENS.PROFILE_SCREEN
        except:
            self.current = LoginScreen.SCREEN_NAME
