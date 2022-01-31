import datetime

from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder
from kivymd.uix.swiper import MDSwiperItem, MDSwiper
from kivymd.uix.card import MDCard

from controllers.authorization import get_my_profile
from controllers.photo import get_path_to_user_profile_image
from views.base import BaseScreen
from views.meta import SCREENS


Builder.load_file('views/add_new_news_screen/add_new_news_screen.kv')


class AddNewNewsScreen(BaseScreen):
    SCREEN_NAME = SCREENS.ADDNEWNEWS_SCREEN
    post_item = ObjectProperty()

    def __init__(self, **kwargs):
        super(AddNewNewsScreen, self).__init__(**kwargs)

    def on_enter(self, *args):
        self.post_item.clear_widgets()
        self.post_item.add_widget(NewPostWidget())


class NewPostWidget(MDCard):
    author = StringProperty()
    text = StringProperty()
    time = StringProperty()
    profile_picture = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        me = get_my_profile()
        self.author = me["name"] + ' ' + me['surname']
        self.profile_picture = get_path_to_user_profile_image(me['id'])
        self.time = datetime.datetime.now().strftime("%d %b %y  %H:%M")
