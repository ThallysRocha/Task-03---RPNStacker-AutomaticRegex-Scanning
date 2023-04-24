from Regex import Regex
class Token:
    def __init__(self, value):
        
        if (Regex.isNum(value)):
           self.type = "NUM"
        elif(Regex.isOP(value)):
            if (value == "*"):
                self.type = "STAR"
            elif (value == "+"):
                self.type = "PLUS"
            elif (value == "-"):
                self.type = "MINUS"
            elif (value == "/"):
                self.type = "SLASH"
        else:
            raise Exception("Unexpected character: "+value)

        self.lexeme = value
        
    def toString(self):
        return "Token [type=" + self.type + ", lexeme=" + self.lexeme + "]"
