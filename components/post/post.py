from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.swiper import MDSwiperItem
from kivy.lang import Builder

from controllers.photo import get_path_to_user_profile_image, refresh_user_profile_picture, get_post_picture

Builder.load_file('components/post/post.kv')


class PostWidget(MDSwiperItem):
    author = StringProperty()
    time = StringProperty()
    profile_picture = StringProperty()
    post_text = ObjectProperty()
    image = ObjectProperty()

    def __init__(self, author_id: int, post_id: int, author: str, time: str, text: str, **kwargs):
        super().__init__(**kwargs)
        self.author_id = author_id
        self.post_id = post_id
        self.author = author
        self.time = time
        self.post_text.text = text

    def load_pictures(self):
        refresh_user_profile_picture(self.author_id)
        self.profile_picture = get_path_to_user_profile_image(self.author_id)
        self.image.source = get_post_picture(self.author_id, self.post_id)
