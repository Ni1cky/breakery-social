from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.list import TwoLineAvatarIconListItem

Builder.load_file('components/dialog_widget/dialog_widget.kv')


class DialogWidget(TwoLineAvatarIconListItem):
    persons_name: str = ObjectProperty()
    persons_surname: str = ObjectProperty()
