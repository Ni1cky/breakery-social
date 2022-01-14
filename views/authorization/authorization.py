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

        token = requests.post('http://127.0.0.1:8000/token', headers={'accept': 'application/json', 'Content-Type': 'application/x-www-form-url-encoded'}, data={ 'grant_type': '', 'username': self.login.text, 'password': self.passw.text, 'scope': '', 'client_id': '', 'client_secret': ''})

        print(token.request.body, token.request.url, token.request.headers)
        print(token.text)




        #self.manager.current = meta.SCREENS.NEWS_SCREEN


class RegisterScreen(BaseScreen):
    pass
