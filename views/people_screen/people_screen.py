from controllers.authorization import get_my_profile
from views import meta
from views.base import BaseScreen
from views.meta import SCREENS, HOST, CLICK_USER
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.filemanager import MDFileManager

Builder.load_file('views/people_screen/people_screen.kv')


class PeopleScreen(BaseScreen):
    SCREEN_NAME = SCREENS.PEOPLE_SCREEN
    name_field = ObjectProperty()
    surname_field = ObjectProperty()
    avatar = ObjectProperty()


    def __init__(self, **kwargs):
        super(PeopleScreen, self).__init__(**kwargs)
        # self.file_manager = MDFileManager(
        #     exit_manager=self.exit_manager,
        #     select_path=self.select_path,
        #     preview=True,
        # )

    def on_enter(self, *args):
        user = CLICK_USER
        self.name_field.text = user.NAME
        self.surname_field.text = user.SURNAME

    def go_to_his_news_screen(self):
        self.manager.current = meta.SCREENS.MY_NEWS_SCREEN

    def load_dialog(self):
        pass


