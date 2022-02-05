from dataclasses import dataclass


@dataclass
class SCREENS:
    LOGIN_SCREEN = 'LoginScreen'
    REGISTER_SCREEN = 'RegisterScreen'
    MAINMENU_SCREEN = 'MainMenuScreen'
    MESSAGE_SCREEN = 'MessageScreen'
    PROFILE_SCREEN = 'ProfileScreen'
    PEOPLE_SCREEN = 'PeopleScreen'
    NEWS_SCREEN = 'NewsScreen'
    MY_NEWS_SCREEN = 'MyNewsScreen'
    DIALOG_SCREEN = "DialogScreen"
    USERS_SCREEN = 'UsersScreen'
    SUBSCRIBERS_SCREEN = 'SubscribersScreen'
    SUBSCRIPTIONS_SCREEN = 'SubscriptionsScreen'
    ADDNEWNEWS_SCREEN = 'AddNewNewsScreen'
    LIKES_SCREEN = 'LikesScreen'


class CLICK_USER:
    USER_ID = 0
    LOGIN = ''
    NAME = ''
    SURNAME = ''
    PHOTO = ''
    ADDITIONAL_DATA = ''
    POSTS = []


class HOST:
    URL = 'http://127.0.0.1:8000'


class AUTHORIZATION:
    TOKEN = ''
