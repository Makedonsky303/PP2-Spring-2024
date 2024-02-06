class Shape:
    def __init__(self,area=0):
        self.area = area
    def printArea(self):
        print(self.area)

class Rectangle(Shape):
    def __init__(self,width,length,area=0):
        self.width = width
        self.length = length
        self.area = area
    def computeArea(self):
        self.area = self.width * self.length

r = Rectangle(3,4)
r.computeArea()
r.printArea()