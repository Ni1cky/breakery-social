from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.swiper import MDSwiperItem
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

from controllers.photo import get_path_to_user_profile_image, refresh_user_profile_picture, get_post_picture
from controllers.user import get_user
from controllers.post import get_post_by_id, get_post_likes, add_like, remove_like
from controllers.authorization import get_my_profile

Builder.load_file('components/post/post.kv')


class PostWidget(MDSwiperItem):
    author = StringProperty()
    time = StringProperty()
    profile_picture = ObjectProperty()
    post_text = ObjectProperty()
    image = ObjectProperty()
    like_icon = ObjectProperty()
    cnt_box = ObjectProperty()
    like_cnt = 0
    counter = None
    cur_user_id = 0

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

        self.cur_user_id = get_my_profile()['id']
        users = get_post_likes(self.post_id)
        self.like_cnt = len(users)
        if users:
            self.counter = MDLabel(text=f"{len(users)}")
            self.cnt_box.add_widget(self.counter)
            users_ids = [user['id'] for user in users]
            if self.cur_user_id in users_ids:
                self.like_icon.icon_color = [1, 0, 0, 1]

    def add_like(self):
        self.like_cnt += 1
        self.like_icon.icon_color = [1, 0, 0, 1]
        add_like(self.cur_user_id, self.post_id)
        if self.like_cnt == 1:
            self.counter = MDLabel(text='1')
            self.cnt_box.add_widget(self.counter)
        else:
            self.counter.text = f"{self.like_cnt}"

    def remove_like(self):
        self.like_cnt -= 1
        self.like_icon.icon_color = [0, 0, 0, 1]
        remove_like(self.cur_user_id, self.post_id)
        if self.like_cnt == 0:
            self.cnt_box.remove_widget(self.counter)
            self.counter = None
        else:
            self.counter.text = f"{self.like_cnt}"
