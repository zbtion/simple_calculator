
class Controller:
    def __init__(self, screen):
        self.screen = screen
    
    def recv_message(self, message):
        if message == "C":
            self.screen.reset_label()
        elif message == "=":
            try:
                self.screen.set_label(str(eval(self.screen.GetLabel())))
            except:
                self.screen.error_label()
        else:
            self.screen.add_label(message)
        