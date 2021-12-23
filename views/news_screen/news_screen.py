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


# MDSwiper

class NewsScreen(BaseScreen):
    SCREEN_NAME = SCREENS.NEWS_SCREEN
    #post_item = ObjectProperty()
    post_item = MDSwiper()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.post_item.size_transition()
        #RiseInTransition()
        for _ in range(4):
            new_post = PostWidget(
                post=Post(id=1, text="ыафждыалфждыажцдуьэж", author="Gosha", time_send=datetime(2019, 6, 1, 12, 22)))
            self.post_item.add_widget(new_post)
            # new_post._dismiss_size()

    def on_enter(self, *args):
        super().on_enter(*args)
        self.post_item._reset_size()

    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget)
        # self.post_item.swipe_right()
        # self.post_item._selected = 0
        # self.post_item._reset_size()
