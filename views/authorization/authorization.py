from kivy.lang import Builder
from views.base import BaseScreen
from views import meta

Builder.load_file('views/authorization/authorization.kv')


class LoginScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.LOGIN_SCREEN

    def go_to_main_screen(self):
        self.manager.current = meta.SCREENS.MAINMENU_SCREEN


class RegisterScreen(BaseScreen):
    pass
