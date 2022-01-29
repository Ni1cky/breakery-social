from views import meta
from views.base import BaseScreen
from views.meta import SCREENS, HOST
from kivy.lang import Builder
from kivymd.uix.swiper import MDSwiperItem, MDSwiper
from kivy.properties import ObjectProperty
from kivymd.uix.filemanager import MDFileManager
import requests

Builder.load_file('views/add_new_news_screen/add_new_news_screen.kv')


class AddNewNewsScreen(BaseScreen):
    SCREEN_NAME = SCREENS.ADDNEWNEWS_SCREEN
    post_item = MDSwiper()
    def __init__(self, **kwargs):
        super(AddNewNewsScreen, self).__init__(**kwargs)
        self.post_item.add_widget(MDSwiperItem)

# class Item(MDSwiperItem):
#     pass