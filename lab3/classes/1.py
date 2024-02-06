class myString:
    def __init__(self):
        self.myStr = ""
    def getString(self):    
        self.myStr = input()
        return self.myStr
    def printString(self):
        print (self.myStr)

p = myString()

p.getString()
p.printString()