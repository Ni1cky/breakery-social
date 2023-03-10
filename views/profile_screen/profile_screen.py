import platform
from typing import Union, NoReturn

from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from controllers.authorization import get_my_profile
from controllers.photo import set_user_profile_picture, get_path_to_user_profile_image, \
    refresh_user_profile_picture, FOLDER_WITH_PHOTOS
from controllers.user import update_user
from views import meta
from views.base import BaseScreen
from views.meta import SCREENS

Builder.load_file('views/profile_screen/profile_screen.kv')


class Content(MDBoxLayout):
    label_color = ObjectProperty()
    red = ObjectProperty()
    green = ObjectProperty()
    blue = ObjectProperty()
    cancel_button = ObjectProperty()
    done_button = ObjectProperty()

    def __init__(self, backdrop, **kwargs):
        super(Content, self).__init__(**kwargs)
        self.backdrop = backdrop
        self.done_button.md_bg_color = backdrop.back_layer_color
        self.cancel_button.icon_color = backdrop.back_layer_color

    def on_open(self, *args):
        self.label_color.canvas.clear()
        self.done_button.md_bg_color = (self.red.value / 255, self.green.value / 255, self.blue.value / 255)
        self.cancel_button.icon_color = (self.red.value / 255, self.green.value / 255, self.blue.value / 255)
        self.red.color = self.green.color = self.blue.color = (self.red.value / 255, self.green.value / 255, self.blue.value / 255)

        with self.label_color.canvas:
            Color(self.red.value / 255, self.green.value / 255, self.blue.value / 255)
            Rectangle(size=self.label_color.size, pos=self.label_color.pos)

    def save(self):
        rgb = (self.red.value / 255, self.green.value / 255, self.blue.value / 255)
        self.backdrop.back_layer_color = rgb
        try:
            with open('saved/color.txt', 'w') as f:
                f.write(str(rgb))
        except:
            pass
        self.parent.parent.parent.dismiss()

    def set_default_theme(self):
        self.backdrop.back_layer_color = [0.28, 0.24, 0.55, 1]
        self.done_button.md_bg_color = [0.28, 0.24, 0.55, 1]
        self.cancel_button.icon_color = [0.28, 0.24, 0.55, 1]
        self.parent.parent.parent.dismiss()

    def close(self):
        self.parent.parent.parent.dismiss()


class ProfileScreen(BaseScreen):
    SCREEN_NAME = SCREENS.PROFILE_SCREEN
    name_field = ObjectProperty()
    surname_field = ObjectProperty()
    picture = ObjectProperty()
    edit_buttons = ObjectProperty()
    save_button = None
    close_button = None
    edit_mode_is_enable = False
    dialog = None

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

    def open_color_picker(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title='Color',
                type='custom',
                content_cls=Content(self.parent.parent.parent.parent.parent),
                # buttons=[
                #     MDIconButton(icon='close-circle-outline', on_release=self.close_color_picker_without_saving),
                #     MDIconButton(icon='arrow-u-left-top', on_release=self.set_default_theme_color),
                # ]
            )
        # self.dialog.bind(on_dismiss=self.close_color_picker)
        self.dialog.open()

    def close_color_picker_without_saving(self, i):
        self.dialog.dismiss()

    def set_default_theme_color(self, i):
        self.dialog.content_cls.paint.back_layer_color = [0.28, 0.24, 0.55, 1]
        self.dialog.dismiss()

    def close_color_picker(self, i):
        rgb = (self.dialog.content_cls.red.value / 255, self.dialog.content_cls.green.value / 255, self.dialog.content_cls.blue.value / 255)
        self.dialog.content_cls.paint.back_layer_color = rgb
        try:
            with open('saved/color.txt', 'w') as f:
                f.write(str(rgb))
        except:
            pass
