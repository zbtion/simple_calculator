
class Controller:
    def __init__(self, screen):
        self.screen = screen
        self.exp = ""
        self.cur = ""
    
    def recv_message(self, message):
        if message == "C" or self.cur == "Error":
            self.exp = ""
            self.cur = ""

        elif message == "del":
            if self.cur != "":
                self.cur = self.cur[:-1]
            else:
                self.exp = self.exp[:-1]

        elif message == "=":
            try:
                self.cur = str(eval(self.exp+self.cur))
            except:
                self.cur = "Error"
            self.exp = ""
                
        
        elif message == "+/-":
            if not self.is_operator(self.cur):
                self.cur = str(-1 * float(self.cur))
            else:
                self.exp += self.cur
                self.cur = "-"
    
        elif message == ".":
            if not self.is_operator(self.cur):
                if "." not in self.cur:
                    self.cur += "."
            else:
                self.exp += self.cur
                self.cur = "0."

        elif self.is_operator(message):
            if not self.is_operator(self.cur):
                self.exp += self.cur                
            self.cur = message
        
        else:
            self.cur += message

        self.screen.set_label(self.exp + self.cur)

    def is_operator(self, message):
        return message in "+-*/%"
        