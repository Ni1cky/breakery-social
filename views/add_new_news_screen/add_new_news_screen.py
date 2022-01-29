from kivy.properties import StringProperty

from views.base import BaseScreen
from views.meta import SCREENS
from kivy.lang import Builder
from kivymd.uix.swiper import MDSwiperItem, MDSwiper


Builder.load_file('views/add_new_news_screen/add_new_news_screen.kv')


class AddNewNewsScreen(BaseScreen):
    SCREEN_NAME = SCREENS.ADDNEWNEWS_SCREEN
    post_item = MDSwiper()
    def __init__(self, **kwargs):
        super(AddNewNewsScreen, self).__init__(**kwargs)

    def on_enter(self, *args):
        self.post_item.add_widget(MDSwiperItem())
        self.post_item.add_widget(NewPostWidget())
        self.post_item.add_widget(MDSwiperItem())
        self.post_item.set_current(1)

class NewPostWidget(MDSwiperItem):
    author = StringProperty()
    text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.author = "Настя 200 метров от вас"


