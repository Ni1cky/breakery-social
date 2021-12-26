from kivy.core.window import Window
from kivymd.app import MDApp
from main_menu.menu import MainMenuScreen

Window.size = (400, 700)


class SocialApp(MDApp):
    current_user_id = 1

    def build(self):
        return MainMenuScreen()


if __name__ == '__main__':
    SocialApp().run()
