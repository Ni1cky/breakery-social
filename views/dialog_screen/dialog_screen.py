import datetime
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.textfield import MDTextField
from controllers.photo import refresh_user_profile_picture, get_path_to_user_profile_image
from store.models.models import MessageCreate
from kivymd.uix.list import TwoLineAvatarIconListItem, ImageLeftWidget, MDList
from controllers.authorization import get_my_profile
from controllers.dialog import get_dialog_by_id
from controllers.user import get_user
from views import meta
from views.base import BaseScreen
from views.meta import SCREENS, CLICK_USER
from controllers.message import get_time_send_sorted_message, create_message
from components.message.message import MessageWidget

Builder.load_file('views/dialog_screen/dialog_screen.kv')


class DialogScreen(BaseScreen):
    SCREEN_NAME = SCREENS.DIALOG_SCREEN
    scrollable_messages: MDList = ObjectProperty()
    header: TwoLineAvatarIconListItem = ObjectProperty()
    message_text: MDTextField = ObjectProperty()
    picture: ImageLeftWidget = ObjectProperty()
    card = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog_data = None

    def on_enter(self, *args):
        user = CLICK_USER
        refresh_user_profile_picture(user.USER_ID)
        self.picture.source = get_path_to_user_profile_image(user.USER_ID)
        self.picture.reload()
        self.scrollable_messages.clear_widgets()
        self.scrollable_messages.scroll_y = 0

    def get_validate_message(self, recipient_id):
        current_user = get_my_profile()
        messages = get_time_send_sorted_message(current_user["id"], recipient_id)
        for message in messages:
            if message.sender_id == current_user["id"]:
                message.send_from_me = True
            else:
                message.send_from_me = False
        return messages

    def reload_messages(self):
        current_user = get_my_profile()
        messages = self.get_validate_message(self.dialog_data["another_user_id"])
        for i in range(len(self.scrollable_messages.children), len(messages)):
            message = messages[i]
            data = message.dict()
            item = MessageWidget(message.text, message.time_send.strftime("%d %b %y  %H:%M"))
            item.size_hint_x = None
            item.width = self.width - 20

            if data["sender_id"] == current_user["id"]:
                item.send_from_me = 1
                item.card.md_bg_color = self.parent.parent.parent.parent.parent.back_layer_color[:3] + [.3]
            else:
                item.send_from_me = 0
                item.card.md_bg_color = [.7, .7, .7, 1]
            self.scrollable_messages.add_widget(item)

    def send_message(self):
        current_user = get_my_profile()
        message = MessageCreate(
            text=self.message_text.text,
            time_send=str(datetime.datetime.now()),
            sender_id=current_user["id"],
            dialog_id=self.dialog_data["dialog_id"]
        )
        create_message(message)
        self.message_text.text = ''

    def load_dialog(self, dialog_id: int):
        current_user = get_my_profile()
        self.dialog_data = None
        dialog = get_dialog_by_id(dialog_id)
        if dialog.user1_id == current_user["id"]:
            self.dialog_data = {"current_user_id": dialog.user1_id, "another_user_id": dialog.user2_id}
            another_user = get_user(dialog.user2_id)
            self.header.text = f"{another_user['name']} {another_user['surname']}"
        else:
            self.dialog_data = {"current_user_id": dialog.user2_id, "another_user_id": dialog.user1_id}
            another_user = get_user(dialog.user1_id)
            self.header.text = f"{another_user['name']} {another_user['surname']}"
        self.dialog_data["dialog_id"] = dialog.id

    def go_to_dialogs(self):
        self.manager.current = meta.SCREENS.MESSAGE_SCREEN

    def go_to_profile(self):
        self.manager.current = meta.SCREENS.PEOPLE_SCREEN
