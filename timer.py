from kivy.clock import Clock
from kivy.uix.widget import Widget


class Timer(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.event = Clock.schedule_interval(self.update_messages, 1)

    def update_messages(self):
        pass
