from kivy.properties import ObjectProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from components.dialog_widget.dialog_widget import DialogWidget
from views.base import BaseScreen
from views.meta import SCREENS
from kivy.lang import Builder

Builder.load_file('views/message_screen/message_screen.kv')


class MessageScreen(BaseScreen):
    SCREEN_NAME = SCREENS.MESSAGE_SCREEN
    dialogs_list: RecycleBoxLayout = ObjectProperty()
    dialogs_recycle_view: RecycleView = ObjectProperty()

    def add_dialog_widget(self, dialog_widget: DialogWidget):
        self.dialogs_recycle_view.data.append({"dialog_id": dialog_widget.dialog.id})
