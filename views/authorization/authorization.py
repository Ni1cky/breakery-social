from kivy.lang import Builder
from kivy.properties import ObjectProperty
import requests
from requests import Request

from views.base import BaseScreen
from views import meta

Builder.load_file('views/authorization/authorization.kv')


class LoginScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.LOGIN_SCREEN
    login = ObjectProperty()
    passw = ObjectProperty()



    def go_to_main_screen(self):
        token = requests.post('http://127.0.0.1:8000/token',
                              data={'grant_type': '', 'username': self.login.text, 'password': self.passw.text,
                                    'scope': '', 'client_id': '', 'client_secret': ''})

        if token.json() != None:
            meta.AUTHORIZATION.LOGIN = self.login.text
            meta.AUTHORIZATION.PASSWORD = self.passw.text
            self.manager.current = meta.SCREENS.PROFILE_SCREEN

    def go_to_registration_screen(self):
        self.manager.current = meta.SCREENS.REGISTER_SCREEN




