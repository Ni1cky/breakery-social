from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextField
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from controllers.authorization import get_token
from views.base import BaseScreen
from views import meta
from kivymd.uix.snackbar import Snackbar
Builder.load_file('views/authorization/authorization.kv')


class LoginScreen(BaseScreen):
    SCREEN_NAME = meta.SCREENS.LOGIN_SCREEN
    login: MDTextField = ObjectProperty()
    passw: MDTextField = ObjectProperty()
    remember_me: MDCheckbox = ObjectProperty()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.snackbar = None
    def on_enter(self, *args):
        self.login.text = ''
        self.passw.text = ''
        try:
            with open('saved/color.txt', 'r') as f:
                f = list(map(float,f.read()[1:-1].split(', ')))
                self.parent.parent.parent.parent.parent.back_layer_color = f
        except:
            print(1)

    def go_to_main_screen(self):

        self.snackbar = Snackbar(text="Wrong login or password!",snackbar_animation_dir="Top",)
        access_token = get_token(self.login.text, self.passw.text)
        if access_token != None:
            if self.remember_me.active:
                f = open('saved\\access_token', 'w')
                f.write(access_token)
                f.close()
            self.manager.current = meta.SCREENS.PROFILE_SCREEN
        else:
            self.snackbar.open()

    def go_to_registration_screen(self):
        self.manager.current = meta.SCREENS.REGISTER_SCREEN



