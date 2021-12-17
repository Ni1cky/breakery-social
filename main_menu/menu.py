from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout

from views import meta


Builder.load_file('main_menu/menu.kv')


class MainMenuScreen(MDBoxLayout):
    manager_screen = ObjectProperty()
    def __init__(self, **kw):
        super().__init__(**kw)

    def go_to_message_screen(self):
        self.manager_screen.current = meta.SCREENS.MESSAGE_SCREEN