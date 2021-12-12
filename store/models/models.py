class User:
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.login = ''
        self.hash_pass = ''
        self.photo = None
        self.id = -1
        self.data = ''

class Message:
    def __init__(self):
        self.text = ''
        self.time_send = ''
        self.is_read = False
        self.is_important = False
        self.is_edited = False
