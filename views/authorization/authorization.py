from kivy.lang import Builder
from kivy.properties import ObjectProperty
import requests
from views.base import BaseScreen
from views import meta

Builder.load_file('views/authorization/authorization.kv')


class LoginScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.LOGIN_SCREEN
    login = ObjectProperty()
    passw = ObjectProperty()
    def go_to_main_screen(self):
        #print(self.login.text, self.passw.text)
        r = requests.get('http://127.0.0.1:8000/users/me')
        print(r.text)
        #self.manager.current = meta.SCREENS.NEWS_SCREEN


class RegisterScreen(BaseScreen):
    pass
