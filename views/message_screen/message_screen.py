from kivymd.uix.list import OneLineListItem, MDList
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from views.base import BaseScreen
from views.meta import SCREENS
from kivy.lang import Builder

Builder.load_file('views/message_screen/message_screen.kv')

class MessageScreen(BaseScreen):
    listBox = ObjectProperty()
    SCREEN_NAME = SCREENS.MESSAGE_SCREEN
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scroll = ScrollView()
        list_view = MDList()
        for i in range(1, 10):
            list_view.add_widget(OneLineListItem(text=f"Имя Фамилия"))
            self.add_widget(MDList())
        scroll.add_widget(list_view)
        self.listBox.add_widget(scroll)





'''class ToDoListApp(MDApp):
    def build(self):
        Window.size = (500, 800)
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
'''