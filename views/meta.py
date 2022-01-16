from dataclasses import dataclass


@dataclass
class SCREENS:
    LOGIN_SCREEN = 'LoginScreen'
    REGISTER_SCREEN = 'RegisterScreen'
    MAINMENU_SCREEN = 'MainMenuScreen'
    MESSAGE_SCREEN = 'MessageScreen'
    PROFILE_SCREEN = 'ProfileScreen'
    NEWS_SCREEN = 'NewsScreen'
    DIALOG_SCREEN = "DialogScreen"

class AUTHORIZATION:
    LOGIN = ''
    PASSWORD = ''
