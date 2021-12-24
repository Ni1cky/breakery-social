from kivy.properties import StringProperty
from kivymd.uix.swiper import MDSwiperItem
from store.models.models import Post
from kivy.lang import Builder

Builder.load_file('components/post/post.kv')

class PostWidget(MDSwiperItem):
    author = StringProperty()
    text = StringProperty()
    def __init__(self, post: Post, **kwargs):
        super().__init__(**kwargs)
        self.text = post.text
        self.author = post.author
        self.time_send = post.time_send



