import math
import string

from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file('components/message/message.kv')

RU = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
ru = 'йцукенгшщзхъфывапролджэячсмитьбю'


class MessageWidget(MDBoxLayout):
    send_from_me = NumericProperty()
    message_label = ObjectProperty()
    time = ObjectProperty()

    def __init__(self, message_text, time_send, **kwargs):
        super(MessageWidget, self).__init__(**kwargs)
        self.message_label.text = message_text + '\n' +\
                                  '                                              ' + '[size=10]' + time_send + '[/size]'
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
