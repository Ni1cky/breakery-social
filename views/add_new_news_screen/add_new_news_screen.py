import datetime
import platform

from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.snackbar import Snackbar

from controllers.authorization import get_my_profile
from controllers.photo import get_path_to_user_profile_image
from controllers.post import add_post, DATE_FORMAT
from views.base import BaseScreen
from views.meta import SCREENS


Builder.load_file('views/add_new_news_screen/add_new_news_screen.kv')

NO_IMAGE = 'img/image-plus.png'


class AddNewNewsScreen(BaseScreen):
    SCREEN_NAME = SCREENS.ADDNEWNEWS_SCREEN
    post_item = ObjectProperty()

    def __init__(self, **kwargs):
        super(AddNewNewsScreen, self).__init__(**kwargs)
        self.post = None

    def on_enter(self, *args):
        self.post_item.clear_widgets()
        self.post = NewPostWidget()
        self.post_item.add_widget(self.post)

    def go_to_profile_screen(self):
        self.manager.current = SCREENS.PROFILE_SCREEN

    def check_and_publish_post(self):
        if not self.post.post_text.text and self.post.image.source == NO_IMAGE:
            Snackbar(text='You must fill in at least one of the fields!', snackbar_animation_dir="Top").open()
            return
        image = '' if self.post.image.source == NO_IMAGE else self.post.image.source
        add_post(self.post.author_id, self.post.post_text.text, self.post.time, image)
        self.go_to_profile_screen()


class NewPostWidget(MDCard):
    author = StringProperty()
    time = StringProperty()
    image = ObjectProperty()
    post_text = ObjectProperty()
    profile_picture = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        me = get_my_profile()
        self.author_id = me['id']
        self.author = me["name"] + ' ' + me['surname']
        self.profile_picture.source = get_path_to_user_profile_image(me['id'])
        self.time = datetime.datetime.now().strftime(DATE_FORMAT)
        self.image.source = NO_IMAGE
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

    def open_file_manager(self):
        os = platform.system()
        if os == "Linux":
            self.file_manager.show("/home")
        else:
            self.file_manager.show("C:\\")

    def select_path(self, path):
        self.exit_manager()
        self.image.source = path

    def exit_manager(self, *args):
        self.file_manager.close()
