class Regex:
    def isNum(value:str):
        if(value.isnumeric()):
            return True
        else:
            return False

    def isOP(value:str):
        if("*/-+".find(value)==-1):
            return False
        else:
            return True