from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.selectioncontrol import MDCheckbox

from controllers.authorization import get_token
from views.base import BaseScreen
from views import meta

Builder.load_file('views/authorization/authorization.kv')


class LoginScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.LOGIN_SCREEN
    login = ObjectProperty()
    passw = ObjectProperty()
    remember_me: MDCheckbox = ObjectProperty()

    def on_enter(self, *args):

        self.login.text = ''
        self.passw.text = ''


    def go_to_main_screen(self):
        access_token = get_token(self.login.text, self.passw.text)
        if access_token != None:
            if self.remember_me.active:
                f = open('saved\\access_token', 'w')
                f.write(access_token)
                f.close()
            self.manager.current = meta.SCREENS.PROFILE_SCREEN
        else:
            pass
            # неправильный логин или пароль

    def go_to_registration_screen(self):
        self.manager.current = meta.SCREENS.REGISTER_SCREEN
