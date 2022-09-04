class Viber:
    mslist = []
    def add_message(msg):
        mslist += [msg]
    @classmethod
    def remove_message(cls, msg):
        cls.mslist.remove(msg)
    @classmethod
    def set_like(cls, msg):
        msg.fl_key = not msg.fl_key
    @classmethod
    def show_last_message(cls, number):
        print(cls.mslist[-number:])
    @classmethod
    def total_messages(cls):
        return len(cls.mslist)


class Message:
    def __init__(self, text, fl_like = False):
        self.text = text
        self.fl_like = fl_like
Viber.add_message(Message('))