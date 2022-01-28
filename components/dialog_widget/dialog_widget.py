from kivy.lang import Builder
from kivymd.uix.list import TwoLineAvatarIconListItem
from controllers.authorization import get_my_profile
from controllers.dialog import get_dialog_by_id
from controllers.user import get_user
from store.models.models import User

Builder.load_file('components/dialog_widget/dialog_widget.kv')


class DialogWidget(TwoLineAvatarIconListItem):
    def __init__(self, dialog_id: int, **kwargs):
        super().__init__(**kwargs)
        self.dialog = get_dialog_by_id(dialog_id)
        self.init_text()

    def init_text(self):
        current_user = User(**get_my_profile())
        second_person_id = self.dialog.user1_id if current_user.id != self.dialog.user1_id else self.dialog.user2_id
        second_person = User(**get_user(second_person_id))
        self.text = f"{second_person.name} {second_person.surname}"
