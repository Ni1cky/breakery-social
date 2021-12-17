from kivy.core.window import Window
from kivymd.app import MDApp
from screen_manager import MainManager
Window.size = (400, 700)


class SocialApp(MDApp):

    def build(self):
        return MainManager()


if __name__ == '__main__':
    SocialApp().run()
