from kivy.core.window import Window
from kivymd.app import MDApp
from screen_manager import Manager
from main_menu.menu import MainMenuScreen
from views import meta

Window.size = (400, 700)

class SocialApp(MDApp):

    def build(self):
        return MainMenuScreen()


if __name__ == '__main__':
    SocialApp().run()

