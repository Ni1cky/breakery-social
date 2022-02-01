from kivy.lang import Builder
from kivy.properties import ObjectProperty

from controllers.post import get_sorted_user_posts
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

    def on_enter(self, *args):
        super().on_enter(*args)
        self.post_item.children[0].clear_widgets()
        me = get_user(self.user_id)
        posts = get_sorted_user_posts(me['id'])
        for post in posts:
            self.post_item.add_widget(PostWidget(me['id'], post['id']))
        self.loaded = 0
        self.ind = 1

        for i in range(min(2, len(posts))):
            self.post_item.children[0].children[-(i + 1)].children[0].load_data()
            self.loaded += 1

        if len(posts):
            self.post_item.set_current(0)

        self.post_item._reset_size()

    def inc_ind(self):
        self.ind += 1
        if self.ind == self.loaded and self.loaded < len(self.post_item.children[0].children):
            self.post_item.children[0].children[-(self.loaded + 1)].children[0].load_data()
            self.loaded += 1

    def dec_ind(self):
        self.ind -= 1
