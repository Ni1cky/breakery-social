from tkinter import Image

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem, MDList
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.list import TwoLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget


class MainMenuScreen(Screen):
    listBox = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        scroll = ScrollView()
        list_view = MDList()
        for i in range(1, 10):
            list_view.add_widget(OneLineListItem(text=f"Имя Фамилия"))
            self.add_widget(MDList())
        scroll.add_widget(list_view)
        self.listBox.add_widget(scroll)

class ToDoListApp(MDApp):
    def build(self):
        Window.size = (700, 1000)
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='main_menu_screen'))
        sm.add_widget(EditingInputScreenTemplate(name='goodbye_screen'))
        return sm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class EditingInputScreenTemplate(Screen):
    pass


if __name__ == '__main__':
    ToDoListApp().run()
