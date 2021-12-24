from kivy.lang import Builder
from kivy.properties import ObjectProperty
from views import meta
from views.base import BaseScreen

Builder.load_file('main_menu/menu.kv')


class MainMenuScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.MAINMENU_SCREEN
    manager_screen = ObjectProperty()
    backdrop = ObjectProperty()
    backdrop_front = ObjectProperty()
    button_profile = ObjectProperty()
    button_news = ObjectProperty()
    button_message = ObjectProperty()
    is_backdrop_front_open = True

    def __init__(self, **kw):
        super().__init__(**kw)
        self.backdrop.bind(on_open=self.front_backdrop_closing)
        self.backdrop.bind(on_close=self.front_backdrop_opening)

    def front_backdrop_closing(self, instance):
        self.is_backdrop_front_open = False

    def front_backdrop_opening(self, instance):
        self.is_backdrop_front_open = True

    def go_to_message_screen(self):
        if not self.is_backdrop_front_open:
            self.manager_screen.current = meta.SCREENS.MESSAGE_SCREEN

    def go_to_profile_screen(self):
        if not self.is_backdrop_front_open:
            self.manager_screen.current = meta.SCREENS.PROFILE_SCREEN

    def go_to_news_screen(self):
        if not self.is_backdrop_front_open:
            self.manager_screen.current = meta.SCREENS.NEWS_SCREEN

    def open_menu_backdrop(self):
        if not self.is_backdrop_front_open:
            if self.manager_screen.current != meta.SCREENS.LOGIN_SCREEN:
                self.backdrop.open()

    def move_menu_backdrop(self):
        if self.manager_screen.current != meta.SCREENS.LOGIN_SCREEN:
            self.backdrop.open()
