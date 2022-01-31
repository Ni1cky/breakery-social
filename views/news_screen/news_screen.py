from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import RiseInTransition
from kivymd.uix.swiper import MDSwiper

from components.post.post import PostWidget
from controllers.authorization import get_my_profile
from controllers.post import get_sorted_subscriptions_posts, get_sorted_other_posts
from controllers.user import get_user
from store.models.models import Post
from views.base import BaseScreen
from views.meta import SCREENS

Builder.load_file('views/news_screen/news_screen.kv')


class NewsScreen(BaseScreen):
    SCREEN_NAME = SCREENS.NEWS_SCREEN
    post_item = ObjectProperty()
    loaded = 0
    ind = 0

    def on_enter(self, *args):
        super().on_enter(*args)
        me = get_my_profile()
        subscriptions_posts = get_sorted_subscriptions_posts(me['id'])
        other_posts = get_sorted_other_posts(me['id'])
        posts = subscriptions_posts + other_posts
        for post in posts:
            user = get_user(post['author_id'])
            author = user['name'] + ' ' + user['surname']
            self.post_item.add_widget(PostWidget(user['id'], post['id'], author, post['time_created'], post['text']))
        self.loaded = 0
        self.ind = 1

        for i in range(min(2, len(posts))):
            self.post_item.children[0].children[-(i + 1)].children[0].load_pictures()
            self.loaded += 1

        if len(posts):
            self.post_item.set_current(0)

        self.post_item._reset_size()

    def inc_ind(self):
        self.ind += 1
        if self.ind == self.loaded and self.loaded < len(self.post_item.children[0].children):
            self.post_item.children[0].children[-(self.loaded + 1)].children[0].load_pictures()
            self.loaded += 1

    def dec_ind(self):
        self.ind -= 1
