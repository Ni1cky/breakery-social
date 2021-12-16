from kivy.uix.screenmanager import Screen


class BaseScreen(Screen):
    SCREEN_NAME = ''

    def __init__(self, **kw):
        super().__init__(name=self.SCREEN_NAME, **kw)
