from kivy.lang import Builder
from kivy.properties import ObjectProperty
import requests
from requests import Request

from controllers.authorization import get_token
from views.base import BaseScreen
from views import meta

Builder.load_file('views/authorization/authorization.kv')


class LoginScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.LOGIN_SCREEN
    login = ObjectProperty()
    passw = ObjectProperty()


    def go_to_main_screen(self):
        if get_token(self.login.text, self.passw.text) != None:
            self.manager.current = meta.SCREENS.PROFILE_SCREEN

    def go_to_registration_screen(self):
        self.manager.current = meta.SCREENS.REGISTER_SCREEN




