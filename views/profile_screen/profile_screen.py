import platform

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDIconButton
from kivymd.uix.filemanager import MDFileManager

from controllers.authorization import get_my_profile
from controllers.photo import set_user_profile_picture, get_path_to_user_profile_image, \
    refresh_user_profile_picture, FOLDER_WITH_PHOTOS
from controllers.user import update_user
from views import meta
from views.base import BaseScreen
from views.meta import SCREENS

Builder.load_file('views/profile_screen/profile_screen.kv')


class ProfileScreen(BaseScreen):
    SCREEN_NAME = SCREENS.PROFILE_SCREEN
    name_field = ObjectProperty()
    surname_field = ObjectProperty()
    picture = ObjectProperty()
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

    def on_enter(self, *args):
        # welcome to my GOVNO-CODE
        self.parent.parent.parent.parent.parent.title = "Profile"
        user = get_my_profile()
        self.name_field.text = user["name"]
        self.surname_field.text = user["surname"]
        refresh_user_profile_picture(user["id"])
        self.picture.source = get_path_to_user_profile_image(user['id'])
        self.picture.reload()

    def go_to_my_news_screen(self):
        self.parent.parent.parent.parent.parent.title = "My posts"
        self.manager.current = meta.SCREENS.MY_NEWS_SCREEN
        user = get_my_profile()
        self.manager.get_screen(meta.SCREENS.MY_NEWS_SCREEN).user_id = user['id']

    def go_to_adding_post_screen(self):
        self.parent.parent.parent.parent.parent.title = "New post"
        self.manager.current = meta.SCREENS.ADDNEWNEWS_SCREEN

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
        user = get_my_profile()
        user['name'] = self.name_field.text
        user['surname'] = self.surname_field.text
        set_user_profile_picture(user["id"], self.picture.source)
        update_user(user)
        self.picture.source = get_path_to_user_profile_image(user['id'])
        self.picture.reload()
        self.disable_edit_mode()

    def reset_changes(self, i):
        user = get_my_profile()
        self.name_field.text = user['name']
        self.surname_field.text = user['surname']
        self.picture.source = get_path_to_user_profile_image(user['id'])
        self.picture.reload()
        self.disable_edit_mode()

    def open_file_manager(self):
        os = platform.system()
        if os == "Linux":
            self.file_manager.show("/home")
        else:
            self.file_manager.show("C:\\")

    def select_path(self, path):
        self.exit_manager()
        self.picture.source = path

    def exit_manager(self, *args):
        self.file_manager.close()
