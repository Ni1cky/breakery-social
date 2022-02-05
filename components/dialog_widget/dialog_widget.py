from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import TwoLineAvatarIconListItem

from controllers.user import get_user
from views import meta

Builder.load_file('components/dialog_widget/dialog_widget.kv')


class DialogWidget(TwoLineAvatarIconListItem):
    persons_name: str = ObjectProperty()
    persons_surname: str = ObjectProperty()
    dialog_id: int = ObjectProperty()
    person_id: int = ObjectProperty()
    last_message_text: str = ObjectProperty()
    last_message_time: str = ObjectProperty()

    def on_press(self):
        screen_manager: ScreenManager = self.parent.parent.parent.parent.manager
        dialog_screen = screen_manager.get_screen(meta.SCREENS.DIALOG_SCREEN)
        dialog_screen.load_dialog(self.dialog_id)
        screen_manager.current = meta.SCREENS.DIALOG_SCREEN

        self.update_click_user()

    def update_click_user(self):
        click_user = meta.CLICK_USER
        person_user = get_user(self.person_id)
        click_user.USER_ID = person_user["id"]
        click_user.LOGIN = person_user["login"]
        click_user.NAME = person_user["name"]
        click_user.SURNAME = person_user["surname"]
        click_user.PHOTO = person_user["photo"]
        click_user.ADDITIONAL_DATA = person_user["additional_data"]
