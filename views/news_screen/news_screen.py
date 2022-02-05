from kivy.lang import Builder
from kivy.properties import ObjectProperty

from components.post.post import PostWidget
from controllers.authorization import get_my_profile
from controllers.post import get_sorted_user_posts, get_block_of_all_posts, get_last_post_id, POSTS_BLOCK_SIZE
from controllers.subscription import get_subscriptions_ids
from views.base import BaseScreen
from views.meta import SCREENS

Builder.load_file('views/news_screen/news_screen.kv')


class NewsScreen(BaseScreen):
    SCREEN_NAME = SCREENS.NEWS_SCREEN
    post_item = ObjectProperty()
    my_id = 0
    loaded = 0
    cur_ind = 0
    min_id = 0
    search_subscriptions = True
    my_posts = []
    subscriptions_ids = []

    def on_pre_enter(self, *args):
        self.post_item.children[0].clear_widgets()

    def on_enter(self, *args):
        super().on_enter(*args)
        #self.post_item.children[0].clear_widgets()
        self.my_id = get_my_profile()['id']
        self.search_subscriptions = True
        self.my_posts = get_sorted_user_posts(self.my_id)
        self.subscriptions_ids = get_subscriptions_ids(self.my_id)
        self.min_id = get_last_post_id()
        self.load_block_of_posts()
        self.loaded = 0
        self.cur_ind = 1
        sz = len(self.post_item.children[0].children)

        for i in range(min(2, sz)):
            self.post_item.children[0].children[-(i + 1)].children[0].load_data()
            self.loaded += 1

        if sz:
            self.post_item.set_current(0)

        self.post_item._reset_size()

    def load_block_of_posts(self):
        try:
            if self.min_id > 0:
                if self.search_subscriptions:
                    posts = self.get_block()

                    if len(posts) < POSTS_BLOCK_SIZE:
                        self.min_id = get_last_post_id()
                        self.search_subscriptions = False
                        posts_2 = self.get_block()
                        posts.extend(posts_2)

                else:
                    posts = self.get_block()

                if self.min_id <= 0 and self.search_subscriptions:
                    self.min_id = get_last_post_id()
                    self.search_subscriptions = False

                for post in posts:
                    self.post_item.add_widget(PostWidget(post['author_id'], post['id']))
        except:
            pass

    def get_block(self):
        posts = []
        while len(posts) < POSTS_BLOCK_SIZE:
            block = get_block_of_all_posts(self.min_id)
            if self.search_subscriptions:
                for post in block:
                    if post['author_id'] in self.subscriptions_ids and post['author_id'] != self.my_id:
                        posts.append(post)
            else:
                for post in block:
                    if post['author_id'] not in self.subscriptions_ids and post['author_id'] != self.my_id:
                        posts.append(post)
            self.min_id -= POSTS_BLOCK_SIZE
            if self.min_id <= 0:
                break
        posts.sort(key=lambda x: x['id'], reverse=True)
        return posts

    def inc_ind(self):
        self.cur_ind += 1
        if self.cur_ind == self.loaded and self.loaded < len(self.post_item.children[0].children):
            self.post_item.children[0].children[-(self.loaded + 1)].children[0].load_data()
            self.loaded += 1

        if self.loaded == len(self.post_item.children[0].children):
            self.load_block_of_posts()

    def dec_ind(self):
        self.cur_ind -= 1
