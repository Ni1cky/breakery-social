from kivy.lang import Builder
from kivy.properties import ObjectProperty
import requests
from kivymd.uix.snackbar import Snackbar
from requests import Request
from controllers.photo import set_default_picture
from views.base import BaseScreen
from views import meta
from views.meta import HOST

Builder.load_file('views/authorization/registration.kv')


class RegisterScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.REGISTER_SCREEN

    login = ObjectProperty()
    passw = ObjectProperty()
    your_name = ObjectProperty()
    surname = ObjectProperty()

    def on_enter(self, *args):
        self.your_name.text = ''
        self.surname.text = ''
        self.login.text = ''
        self.passw.text = ''

    def go_to_login_screen(self):
        self.manager.current = meta.SCREENS.LOGIN_SCREEN

    def register(self):
        reg = requests.post(f'{HOST.URL}/auth/register',
                              json={"login": self.login.text, "password_hash": self.passw.text,
                                    "name": self.your_name.text, "surname": self.surname.text,
                                    "photo": "", "additional_data": ""},
                              headers={'accept': 'application/json', 'Content-Type': 'application/json'})
        if reg.text == 'null':
            set_default_picture(self.login.text)
            self.manager.current = meta.SCREENS.LOGIN_SCREEN
        else:
            self.snackbar = Snackbar(text="this login has already been used", snackbar_animation_dir="Top", )
            self.snackbar.open()

