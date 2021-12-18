from views.base import BaseScreen
from views.meta import SCREENS
from kivy.lang import Builder

Builder.load_file('views/profile_screen/profile_screen.kv')


class ProfileScreen(BaseScreen):
    SCREEN_NAME = SCREENS.PROFILE_SCREEN
