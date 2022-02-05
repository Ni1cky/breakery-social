from controllers.authorization import get_my_profile
from controllers.dialog import create_dialog, get_dialog_by_users_ids
from controllers.photo import refresh_user_profile_picture, get_path_to_user_profile_image
from store.models.models import DialogCreate
from views import meta
from views.base import BaseScreen
from views.dialog_screen.dialog_screen import DialogScreen
from views.meta import SCREENS, CLICK_USER
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.filemanager import MDFileManager

Builder.load_file('views/people_screen/people_screen.kv')


class PeopleScreen(BaseScreen):
    SCREEN_NAME = SCREENS.PEOPLE_SCREEN
    name_field = ObjectProperty()
    surname_field = ObjectProperty()
    picture = ObjectProperty()

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

        refresh_user_profile_picture(user.USER_ID)
        self.picture.source = get_path_to_user_profile_image(user.USER_ID)
        self.picture.reload()

    def go_to_his_news_screen(self):
        self.manager.current = meta.SCREENS.MY_NEWS_SCREEN
        user = CLICK_USER
        self.manager.get_screen(meta.SCREENS.MY_NEWS_SCREEN).user_id = user.USER_ID

    def load_dialog(self):
        dialog_screen: DialogScreen = self.manager.get_screen(meta.SCREENS.DIALOG_SCREEN)
        try:
            existing_dialog = get_dialog_by_users_ids(CLICK_USER.USER_ID, get_my_profile()["id"])
        except:
            d = DialogCreate(user1_id=CLICK_USER.USER_ID, user2_id=get_my_profile()["id"])
            create_dialog(d)
        else:
            dialog_screen.load_dialog(existing_dialog.id)
            self.manager.current = meta.SCREENS.DIALOG_SCREEN
            return
        created_dialog = get_dialog_by_users_ids(CLICK_USER.USER_ID, get_my_profile()["id"])
        dialog_screen.load_dialog(created_dialog.id)
        self.manager.current = meta.SCREENS.DIALOG_SCREEN
