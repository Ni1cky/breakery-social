from kivy.lang import Builder
from kivy.properties import ObjectProperty

from controllers.post import get_sorted_user_posts, POSTS_BLOCK_SIZE
from controllers.authorization import get_my_profile
from controllers.user import get_user
from components.post.post import PostWidget
from views.base import BaseScreen
from views.meta import SCREENS

Builder.load_file('views/my_news_screen/my_news_screen.kv')


class MyNewsScreen(BaseScreen):
    SCREEN_NAME = SCREENS.MY_NEWS_SCREEN
    post_item = ObjectProperty()
    user_id = 0
    loaded = 0
    ind = 0
    posts_to_load = []
    min_id = 0
    my_id = 0

    def on_enter(self, *args):
        super().on_enter(*args)
        self.post_item.children[0].clear_widgets()
        self.my_id = get_user(self.user_id)['id']
        self.min_id = 0
        self.posts_to_load = get_sorted_user_posts(self.my_id)
        self.load_block()
        self.loaded = 0
        self.ind = 1

        for i in range(min(2, len(self.post_item.children[0].children))):
            self.post_item.children[0].children[-(i + 1)].children[0].load_data()
            self.loaded += 1

        if len(self.post_item.children[0].children):
            self.post_item.set_current(0)

        self.post_item._reset_size()

    def load_block(self):
        block = self.posts_to_load[self.min_id:self.min_id + POSTS_BLOCK_SIZE]
        self.min_id += POSTS_BLOCK_SIZE

        if not block:
            return

        for post in block:
            self.post_item.add_widget(PostWidget(self.my_id, post['id']))

    def inc_ind(self):
        self.ind += 1
        if self.ind == self.loaded and self.loaded < len(self.post_item.children[0].children):
            self.post_item.children[0].children[-(self.loaded + 1)].children[0].load_data()
            self.loaded += 1

        if self.loaded == len(self.post_item.children[0].children):
            self.load_block()

    def dec_ind(self):
        self.ind -= 1
