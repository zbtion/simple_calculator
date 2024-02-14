
class Controller:
    def __init__(self, screen):
        self.screen = screen
        self.label = ""
        self.current_operator = ""
        self.current_number = ""
    
    def recv_message(self, message):
        if message == "C" or self.label == "Error":
            self.label = ""
        elif message == "del":
            self.label = self.label[:-1]
        elif message == "=":
            try:
                self.label = str(eval(self.label))
            except:
                self.label = "Error"
        elif message == "+/-":
            pass
        else:
            self.label += message
        self.screen.set_label(self.label)
    
    def is_digit(self, message):
        return message in "0123456789"

    def is_operator(self, message):
        return message in "+-*/"
        