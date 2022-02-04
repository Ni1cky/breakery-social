import math
import string

from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file('components/message/message.kv')

from kivy.uix.recycleview.views import RecycleDataViewBehavior
RU = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
ru = 'йцукенгшщзхъфывапролджэячсмитьбю'
# letters = {
#     'q': 31,
#     'w': 23,
#     'e': 31,
#     'r': 51,
#     't': 31,
#     'y': 35,
#     'u': 35,
#     'i': 1,
#     'o': 1,
#     'p': 1,
#     'a': 34,
#     's': 1,
#     'd': 1,
#     'f': 1,
#     'g': 1,
#     'h': 1,
#     'j': 1,
#     'k': 1,
#     'l': 1,
#     'z': 1,
#     'x': 1,
#     'c': 1,
#     'v': 1,
#     'b': 1,
#     'n': 1,
#     'm': 1,
#     'Q': 1,
#     'W': 1,
#     'E': 1,
#     'R': 1,
#     'T': 1,
#     'Y': 1,
#     'U': 1,
#     'I': 1,
#     'O': 1,
#     'P': 1,
#     'A': 1,
#     'S': 1,
#     'D': 1,
#     'F': 1,
#     'H': 1,
#     'J': 1,
#     'K': 1,
#     'L': 1,
#     'Z': 1,
#     'X': 1,
#     'C': 1,
#     'V': 1,
#     'B': 1,
#     'N': 1,
#     'M': 1,
#
# }


class MessageWidget(MDBoxLayout):
    # _latest_data = None
    # _recycle_view = None
    # message_text = StringProperty()
    send_from_me = NumericProperty()
    message_label = ObjectProperty()
    time = ObjectProperty()

    def __init__(self, message_text, time_send, **kwargs):
        super(MessageWidget, self).__init__(**kwargs)
        self.message_label.text = message_text + '\n' +\
                                  '                                              ' + '[size=10]' + time_send + '[/size]'
        # self.time.text = time_send
        cnt = 0
        for c in message_text:
            if c in RU:
                cnt += 1 / 24
            elif c in ru:
                cnt += 1 / 29
            elif c in string.ascii_lowercase:
                cnt += 1 / 35
            elif c in string.ascii_uppercase:
                cnt += 1 / 26
            elif c in string.digits:
                cnt += 1 / 26
            else:
                cnt += 1 / 50
        self.height = math.ceil(cnt + 1) * 35

    # def refresh_view_attrs(self, recycle_view, index, data):
    #     self._recycle_view = recycle_view
    #     if self._latest_data is not None:
    #         self._latest_data["height"] = self.height
    #     self._latest_data = data
    #     super().refresh_view_attrs(recycle_view, index, data)
    #
    # def on_height(self, instance, value):
    #     data = self._latest_data
    #     if data is not None and data["height"] != value:
    #         data["height"] = value
    #         self._recycle_view.refresh_from_data()
