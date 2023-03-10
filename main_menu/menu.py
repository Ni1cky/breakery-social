import os
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.backdrop import MDBackdrop
from screen_manager import Manager
from views import meta
from views.base import BaseScreen
from views.dialog_screen.dialog_screen import DialogScreen
from views.meta import AUTHORIZATION

Builder.load_file('main_menu/menu.kv')


class MainMenuScreen(BaseScreen):
    # app_color = ObjectProperty()
    SCREEN_NAME = meta.SCREENS.MAINMENU_SCREEN
    manager_screen: Manager = ObjectProperty()
    backdrop: MDBackdrop = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.backdrop.bind(on_open=self.front_backdrop_closing)
        self.backdrop.bind(on_close=self.front_backdrop_opening)
        self.is_backdrop_front_open = True
        self.event = Clock.schedule_interval(self.update_messages, 1)
        # self.app_color = "Purple"
        try:
            with open('saved/color.txt', 'r') as f:
                f = list(map(float,f.read()[1:-1].split(', ')))
                self.backdrop.back_layer_color = f
        except:
            print(1)


    def update_messages(self, *args):
        if self.manager_screen.current == meta.SCREENS.DIALOG_SCREEN:
            dialog_screen: DialogScreen = self.manager_screen.current_screen
            dialog_screen.reload_messages()

    def front_backdrop_closing(self, instance):
        self.is_backdrop_front_open = False

    def front_backdrop_opening(self, instance):
        self.is_backdrop_front_open = True

    def go_to_message_screen(self):
        if not self.is_backdrop_front_open:
            if self.manager_screen.current != meta.SCREENS.LOGIN_SCREEN:
                self.manager_screen.current = meta.SCREENS.MESSAGE_SCREEN
                self.backdrop.title = 'Dialogs'
            else:
                self.manager_screen.current = meta.SCREENS.LOGIN_SCREEN
            self.move_menu_backdrop()

    def go_to_dialogue_screen(self):
        if not self.is_backdrop_front_open:
            if self.manager_screen.current != meta.SCREENS.LOGIN_SCREEN:
                self.manager_screen.current = meta.SCREENS.DIALOG_SCREEN
                self.backdrop.title = 'Dialogs'
            else:
                self.manager_screen.current = meta.SCREENS.LOGIN_SCREEN
            self.move_menu_backdrop()

    def go_to_profile_screen(self):
        if not self.is_backdrop_front_open:
            if self.manager_screen.current != meta.SCREENS.LOGIN_SCREEN:
                self.backdrop.title = 'Profile'
                self.manager_screen.current = meta.SCREENS.PROFILE_SCREEN

            else:
                self.manager_screen.current = meta.SCREENS.LOGIN_SCREEN
            self.move_menu_backdrop()

    def go_to_news_screen(self):
        if not self.is_backdrop_front_open:
            if self.manager_screen.current != meta.SCREENS.LOGIN_SCREEN:
                self.manager_screen.current = meta.SCREENS.NEWS_SCREEN
                self.backdrop.title = 'News'
            else:
                self.manager_screen.current = meta.SCREENS.LOGIN_SCREEN
            self.move_menu_backdrop()

    def go_to_likes_screen(self):
        if not self.is_backdrop_front_open:
            if self.manager_screen.current != meta.SCREENS.LOGIN_SCREEN:
                self.manager_screen.current = meta.SCREENS.LIKES_SCREEN
                self.backdrop.title = 'Likes'
            else:
                self.manager_screen.current = meta.SCREENS.LOGIN_SCREEN
            self.move_menu_backdrop()

    def go_to_users_screen(self):
        if not self.is_backdrop_front_open:
            if self.manager_screen.current != meta.SCREENS.LOGIN_SCREEN:
                self.manager_screen.current = meta.SCREENS.USERS_SCREEN
                self.backdrop.title = 'Users'
            else:
                self.manager_screen.current = meta.SCREENS.LOGIN_SCREEN
            self.move_menu_backdrop()

    def go_to_subscribers_screen(self):
        if not self.is_backdrop_front_open:
            if self.manager_screen.current != meta.SCREENS.LOGIN_SCREEN:
                self.manager_screen.current = meta.SCREENS.SUBSCRIBERS_SCREEN
                self.backdrop.title = 'Your Subscribers'
            else:
                self.manager_screen.current = meta.SCREENS.LOGIN_SCREEN
            self.move_menu_backdrop()

    def go_to_subscriptions_screen(self):
        if not self.is_backdrop_front_open:
            if self.manager_screen.current != meta.SCREENS.LOGIN_SCREEN:
                self.manager_screen.current = meta.SCREENS.SUBSCRIPTIONS_SCREEN
                self.backdrop.title = 'Subscriptions'
            else:
                self.manager_screen.current = meta.SCREENS.LOGIN_SCREEN
            self.move_menu_backdrop()

    def open_menu_backdrop(self):
        if not self.is_backdrop_front_open:
            if self.manager_screen.current != meta.SCREENS.LOGIN_SCREEN:
                self.backdrop.open()

    def move_menu_backdrop(self):
        self.backdrop.open()

    def log_out(self):
        if not self.is_backdrop_front_open:
            try:
                self.manager_screen.current = meta.SCREENS.LOGIN_SCREEN
                self.move_menu_backdrop()
                self.backdrop.title = ''
                AUTHORIZATION.TOKEN = ''
                os.remove('saved\\access_token')
            except:
                pass
