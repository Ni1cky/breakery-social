from json import JSONDecodeError

from kivy.properties import ObjectProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from controllers.authorization import get_my_profile
from controllers.dialog import get_users_dialogs
from controllers.message import get_time_send_sorted_message
from controllers.user import get_user
from store.models.models import User
from views.base import BaseScreen
from views.meta import SCREENS
from kivy.lang import Builder

Builder.load_file('views/message_screen/message_screen.kv')


class MessageScreen(BaseScreen):
    SCREEN_NAME = SCREENS.MESSAGE_SCREEN
    dialogs_list: RecycleBoxLayout = ObjectProperty()
    dialogs_recycle_view: RecycleView = ObjectProperty()

    def on_enter(self, *args):
        self.dialogs_recycle_view.data.clear()
        try:
            dialogs_to_load = get_users_dialogs(get_my_profile()["id"])
        except JSONDecodeError:
            return
        for dialog in dialogs_to_load:
            if dialog.user1_id == get_my_profile()["id"]:
                second_persons_id = dialog.user2_id
            else:
                second_persons_id = dialog.user1_id
            second_person = get_user(second_persons_id)

            messages = get_time_send_sorted_message(get_my_profile()["id"], second_persons_id)
            last_message = messages[-1]

            self.dialogs_recycle_view.data.append({
                "persons_name": second_person["name"],
                "persons_surname": second_person["surname"],
                "dialog_id": dialog.id,
                "person_id": second_persons_id,
                "last_message_text": last_message.text,
                "last_message_time": str(last_message.time_send.strftime("%H:%M"))
            })
