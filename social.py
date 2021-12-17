from kivy.core.window import Window
from kivymd.app import MDApp

from screen_manager import Manager

Window.size = (400, 700)


class SocialApp(MDApp):

    def build(self):
        self.manager = Manager()
        return self.manager


if __name__ == '__main__':
    SocialApp().run()
