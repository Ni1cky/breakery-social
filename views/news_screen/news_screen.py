from views.base import BaseScreen
from views.meta import SCREENS
from kivy.lang import Builder

Builder.load_file('views/news_screen/news_screen.kv')


class NewsScreen(BaseScreen):
    SCREEN_NAME = SCREENS.NEWS_SCREEN
