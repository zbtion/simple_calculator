
class Controller:
    def __init__(self, screen):
        self.screen = screen
        self.label = ""
        self.current = ""
    
    def recv_message(self, message):
        if message == "C" or self.label == "Error":
            self.label = ""
            self.current = ""

        elif message == "del":
            if self.current != "":
                self.current = self.current[:-1]
            else:
                self.label = self.label[:-1]

        elif message == "=":
            try:
                self.label = str(eval(self.label+self.current))
            except:
                self.label = "Error"
            self.current = ""
        
        elif message == "+/-":
            pass    # not implemented yet
    
        elif message == ".":
            pass   # not implemented yet

        elif self.is_operator(message):
            if not self.is_operator(self.current):
                self.label += self.current                
            self.current = message
        
        else:
            self.current += message

        self.screen.set_label(self.label + self.current)

    def is_operator(self, message):
        return message in "+-*/%"
        