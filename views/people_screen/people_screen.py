from components.dialog_widget.dialog_widget import DialogWidget
from controllers.authorization import get_my_profile
from controllers.dialog import create_dialog, get_dialog_by_users_ids
from store.models.models import DialogCreate
from views import meta
from views.base import BaseScreen
from views.message_screen.message_screen import MessageScreen
from views.meta import SCREENS, CLICK_USER
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
        message_screen: MessageScreen = self.manager.get_screen(meta.SCREENS.MESSAGE_SCREEN)
        try:
            existing_dialog = get_dialog_by_users_ids(CLICK_USER.USER_ID, get_my_profile()["id"])
        except:
            d = DialogCreate(user1_id=CLICK_USER.USER_ID, user2_id=get_my_profile()["id"])
            create_dialog(d)
            existing_dialog = get_dialog_by_users_ids(CLICK_USER.USER_ID, get_my_profile()["id"])
            message_screen.add_dialog_widget(DialogWidget(existing_dialog.id))
        else:
            dialog_widget = DialogWidget(existing_dialog.id)
            if not self.dialog_widget_exists_in_list(dialog_widget, message_screen):
                message_screen.add_dialog_widget(dialog_widget)

    def dialog_widget_exists_in_list(self, dw: DialogWidget, message_screen: MessageScreen):
        for dialog_widget in message_screen.dialogs_recycle_view.data:
            if dialog_widget["dialog_id"] == dw.dialog.id:
                return True
        return False
