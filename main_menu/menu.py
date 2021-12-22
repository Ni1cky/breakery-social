from kivy.lang import Builder
from kivy.properties import ObjectProperty
from views import meta
from views.base import BaseScreen

Builder.load_file('main_menu/menu.kv')


class MainMenuScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.MAINMENU_SCREEN
    manager_screen = ObjectProperty()
    def __init__(self, **kw):
        super().__init__(**kw)

    def go_to_message_screen(self):
        self.manager_screen.current = meta.SCREENS.MESSAGE_SCREEN

    def go_to_profile_screen(self):
        self.manager_screen.current = meta.SCREENS.PROFILE_SCREEN

    def go_to_news_screen(self):
        self.manager_screen.current = meta.SCREENS.NEWS_SCREEN

