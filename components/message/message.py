from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem
from store.models.models import Message
from kivy.lang import Builder

Builder.load_file('components/message/message.kv')

from kivy.uix.recycleview.views import RecycleDataViewBehavior


class MessageWidget(RecycleDataViewBehavior, BoxLayout):
    _latest_data = None
    _rv = None
    message_text = StringProperty()
    message = ObjectProperty()
    send_from_me = NumericProperty()
    textik = ObjectProperty()

    def refresh_view_attrs(self, rv, index, data):
        self._rv = rv
        if self._latest_data is not None:
            self._latest_data["height"] = self.height
        self._latest_data = data
        print(self._latest_data)
        super(MessageWidget, self).refresh_view_attrs(rv, index, data)

    def on_height(self, instance, value):
        data = self._latest_data
        if data is not None and data["height"] != value:
            data["height"] = value
            self._rv.refresh_from_data()
