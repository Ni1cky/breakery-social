from kivy.lang import Builder
from kivy.properties import ObjectProperty

from views.base import BaseScreen
from views.meta import SCREENS
from components.post.post import PostWidget
from controllers.authorization import get_my_profile
from controllers.post import POSTS_BLOCK_SIZE, get_like_posts

Builder.load_file("views/likes_screen/likes_screen.kv")


class LikesScreen(BaseScreen):
    SCREEN_NAME = SCREENS.LIKES_SCREEN
    post_item = ObjectProperty()
    user_id = 0
    loaded = 0

    ind = 0
    posts_to_load = []
    min_id = 0
    my_id = 0

    def on_pre_enter(self, *args):
        # self.post_item.children[0].clear_widgets()
        pass

    def on_enter(self, *args):
        super().on_enter(*args)
        self.post_item.children[0].clear_widgets()
        self.my_id = get_my_profile()['id']
        self.min_id = 0
        self.posts_to_load = get_like_posts(self.my_id)
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
            self.post_item.add_widget(PostWidget(post['author_id'], post['id']))

    def inc_ind(self):
        self.ind += 1
        if self.ind == self.loaded and self.loaded < len(self.post_item.children[0].children):
            self.post_item.children[0].children[-(self.loaded + 1)].children[0].load_data()
            self.loaded += 1

        if self.loaded == len(self.post_item.children[0].children):
            self.load_block()

    def dec_ind(self):
        self.ind -= 1
