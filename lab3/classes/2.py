class Shape:
    def __init__(self,area=0):
        self.area = area
    def printArea(self):
        print(self.area)

class Square(Shape):
    def __init__(self,length,area=0):
        self.area = area
        self.length = length

s = Shape(10)
s.printArea()
sq = Square(5)
sq.printArea()
print(sq.length)
