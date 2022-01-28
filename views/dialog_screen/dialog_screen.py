from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView

from controllers.authorization import get_my_profile
from store.models.models import Message
from views.base import BaseScreen
from views.meta import SCREENS
from controllers.message import get_time_send_sorted_message

Builder.load_file('views/dialog_screen/dialog_screen.kv')


class DialogScreen(BaseScreen):
    SCREEN_NAME = SCREENS.DIALOG_SCREEN
    scrollable_messages: RecycleView = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scrollable_messages.data = []

        # for i in range(1, 40):
        #     print(len(i * "привет") // 20 * 100)
        #     self.scrollable_messages.data.append({'message_text': i * "привет)",
        #                                                 'time_send': datetime.datetime(2019, 6, 1, 12, 22),
        #                                                 'is_read': False,
        #                                                 'is_important': False,
        #                                                 'is_edited': False,
        #                                           "height": int(max(len(i * "привет") / 40, 1) * 50),
        #                                         'send_from_me': i % 2})

    def get_validate_message(self, recipient_id):
        messages = get_time_send_sorted_message(get_my_profile()["id"], recipient_id)
        # for message in messages:
        #     if message.id == recipient_id:
        #         message.send_from_me = True
        #     else:
        #         message.send_from_me = False
        return messages

    def reload_messages(self):
        messages = self.get_validate_message(2)
        self.scrollable_messages.data = []
        for message in messages:
            message: Message
            data = message.dict()
            data["message_text"] = data.pop("text")
            if data["id"] == current_user.CURRENT_USER_ID:
                data["send_from_me"] = 1
            else:
                data["send_from_me"] = 0
            self.scrollable_messages.data.append(data)
