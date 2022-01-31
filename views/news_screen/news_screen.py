from datetime import datetime

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import RiseInTransition
from kivymd.uix.swiper import MDSwiper

from components.post.post import PostWidget
from store.models.models import Post
from views.base import BaseScreen
from views.meta import SCREENS

Builder.load_file('views/news_screen/news_screen.kv')


class NewsScreen(BaseScreen):
    SCREEN_NAME = SCREENS.NEWS_SCREEN
    post_item = ObjectProperty()

    def on_enter(self, *args):
        super().on_enter(*args)
        self.post_item._reset_size()

    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget)
        # self.post_item.swipe_right()
        # self.post_item._selected = 0
        # self.post_item._reset_size()
