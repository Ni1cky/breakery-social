from kivy.lang import Builder
from kivy.properties import ObjectProperty
import requests
from requests import Request

from views.base import BaseScreen
from views import meta

Builder.load_file('views/authorization/registration.kv')


class RegisterScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.REGISTER_SCREEN

    login = ObjectProperty()
    passw = ObjectProperty()
    your_name = ObjectProperty()
    surname = ObjectProperty()

    def go_to_login_screen(self):
        self.manager.current = meta.SCREENS.LOGIN_SCREEN

    def register(self):
        reg = requests.post('http://127.0.0.1:8000/auth/register',
                              json={"login": self.login.text, "password_hash": self.passw.text,
                                    "name": self.your_name.text, "surname": self.surname.text,
                                    "photo": "", "additional_data": ""},
                              headers={'accept': 'application/json', 'Content-Type': 'application/json'})
        if reg.text == 'null':
            self.manager.current = meta.SCREENS.LOGIN_SCREEN

