from dataclasses import dataclass


@dataclass
class SCREENS:
    LOGIN_SCREEN = 'LoginScreen'
    REGISTER_SCREEN = 'RegisterScreen'
    MAINMENU_SCREEN = 'MainMenuScreen'
    MESSAGE_SCREEN = 'MessageScreen'
    PROFILE_SCREEN = 'ProfileScreen'
    NEWS_SCREEN = 'NewsScreen'
    MY_NEWS_SCREEN = 'MyNewsScreen'
    DIALOG_SCREEN = "DialogScreen"
    USERS_SCREEN = 'UsersScreen'
    SUBSCRIBERS_SCREEN = 'SubscribersScreen'


class AUTHORIZATION:
    TOKEN = ''
