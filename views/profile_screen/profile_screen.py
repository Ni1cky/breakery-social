from views.base import BaseScreen
from views.meta import SCREENS
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDIconButton
from kivymd.uix.filemanager import MDFileManager

Builder.load_file('views/profile_screen/profile_screen.kv')

user_name = "Name"
user_surname = "Surname"
user_avatar_source = "img/profile.jpg"


class ProfileScreen(BaseScreen):
    SCREEN_NAME = SCREENS.PROFILE_SCREEN
    name_field = ObjectProperty()
    surname_field = ObjectProperty()
    avatar = ObjectProperty()
    edit_buttons = ObjectProperty()
    save_button = None
    close_button = None
    edit_mode_is_enable = False

    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

    def enable_edit_mode(self):
        if self.edit_mode_is_enable:
            return
        self.edit_mode_is_enable = True
        self.name_field.disabled = False
        self.surname_field.disabled = False
        self.save_button = MDIconButton(icon='check', on_release=self.save_changes)
        self.close_button = MDIconButton(icon='close', on_release=self.reset_changes)
        self.edit_buttons.add_widget(self.save_button)
        self.edit_buttons.add_widget(self.close_button)

    def disable_edit_mode(self):
        self.edit_mode_is_enable = False
        self.name_field.disabled = True
        self.surname_field.disabled = True
        self.edit_buttons.remove_widget(self.save_button)
        self.edit_buttons.remove_widget(self.close_button)
        self.save_button = None
        self.close_button = None

    def save_changes(self, i):
        global user_name, user_surname, user_avatar_source
        user_name = self.name_field.text
        user_surname = self.surname_field.text
        user_avatar_source = self.avatar.icon
        self.disable_edit_mode()

    def reset_changes(self, i):
        self.name_field.text = user_name
        self.surname_field.text = user_surname
        self.avatar.icon = user_avatar_source
        self.disable_edit_mode()

    def change_avatar(self):
        self.file_manager.show("/home")

    def select_path(self, path):
        self.exit_manager()
        self.avatar.icon = path

    def exit_manager(self, *args):
        self.file_manager.close()
