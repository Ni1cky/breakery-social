from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.swiper import MDSwiperItem
from kivy.lang import Builder

from controllers.photo import get_path_to_user_profile_image, refresh_user_profile_picture, get_post_picture
from controllers.user import get_user
from controllers.post import get_post_by_id

Builder.load_file('components/post/post.kv')


class PostWidget(MDSwiperItem):
    author = StringProperty()
    time = StringProperty()
    profile_picture = ObjectProperty()
    post_text = ObjectProperty()
    image = ObjectProperty()
    like = ObjectProperty()
    like_cnt = 0

    def __init__(self, author_id: int, post_id: int, **kwargs):
        super().__init__(**kwargs)
        self.author_id = author_id
        self.post_id = post_id

    def load_data(self):
        refresh_user_profile_picture(self.author_id)
        self.profile_picture.source = get_path_to_user_profile_image(self.author_id)
        self.image.source = get_post_picture(self.author_id, self.post_id)

        author = get_user(self.author_id)
        self.author = author['name'] + ' ' + author['surname']
        post = get_post_by_id(self.post_id)
        self.time = post['time_created']
        self.post_text.text = post['text']

    def add_like(self):
        self.like_cnt += 1
        self.like.badge_color.icon = f"numeric-{self.like_cnt}"

    def remove_like(self):
        print(0)
