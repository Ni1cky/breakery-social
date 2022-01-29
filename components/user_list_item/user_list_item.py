from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch

from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from views.meta import CLICK_USER
from controllers.subscription import subscribe_to_user, unsubscribe_from_user
from views import meta
from views.people_screen.people_screen import PeopleScreen
from controllers.photo import refresh_user_profile_picture, get_path_to_user_profile_image
Builder.load_file('components/user_list_item/user_list_item.kv')


class RightButton(IRightBodyTouch, MDRaisedButton):
    pass


class UserListItem(OneLineAvatarIconListItem):
    image = ObjectProperty()
    button = ObjectProperty()
    TO_SUBSCRIBE = "Подписаться"
    TO_UNSUBSCRIBE = "Отписаться"

    def __init__(self, user: dict, is_my_subscription: bool, **kwargs):
        super(UserListItem, self).__init__(**kwargs)
        self.user = user
        self.text = f"{user['name']} {user['surname']}"
        self.button.text = self.TO_UNSUBSCRIBE if is_my_subscription else self.TO_SUBSCRIBE
        self.update_button_color()

    def on_press(self):
        CLICK_USER.NAME = self.user['name']
        CLICK_USER.SURNAME = self.user['surname']
        #добавить потом фотографию
        self.parent.parent.parent.manager.current = meta.SCREENS.PEOPLE_SCREEN

    def subscribe(self):
        subscribe_to_user(self.user["id"])
        self.button.text = self.TO_UNSUBSCRIBE
        self.update_button_color()

    def unsubscribe(self):
        unsubscribe_from_user(self.user["id"])
        self.button.text = self.TO_SUBSCRIBE
        self.update_button_color()

    def update_button_color(self):
        if self.button.text == self.TO_SUBSCRIBE:
            self.button.md_bg_color = (0.28, 0.24, 0.55, 1)
            self.button.text_color = (0.96, 1, 0.98, 1)
        else:
            self.button.md_bg_color = (0.57, 0.57, 0.57, 1)
            self.button.text_color = (0.28, 0.24, 0.55, 1)

    def load_image(self):
        refresh_user_profile_picture(self.user['id'])
        self.image.source = get_path_to_user_profile_image(self.user['id'])
