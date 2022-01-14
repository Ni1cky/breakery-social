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
        r = requests.Request('GET', 'http://127.0.0.1:8000/users/me')
        user = self.send(r)
        print(user.text)
        self.manager.current = meta.SCREENS.PROFILE_SCREEN


    def send(self, req: Request):
        token = requests.post('http://127.0.0.1:8000/token',
                              data={'grant_type': '', 'username': self.login.text, 'password': self.passw.text,
                                    'scope': '', 'client_id': '', 'client_secret': ''})
        req.headers[
            'Authorization'] = f"Bearer {token.json()['access_token']}"
        s = requests.Session()
        resp = s.send(req.prepare())
        return resp






class RegisterScreen(BaseScreen):
    pass
