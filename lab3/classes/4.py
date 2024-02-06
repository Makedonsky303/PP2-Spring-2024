class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print("x:",self.x)
        print("y:",self.y) 
    def move(self,newX,newY):
        self.x = newX
        self.y = newY
    def dist(self, secondX, secondY):
        xDiff = abs(self.x-secondX)
        yDiff = abs(self.y-secondY)
        distance = (xDiff**2 + yDiff**2)**0.5
        return distance

p = Point(34,55)
p.show()   
p.move(3,4)
print(p.dist(0,0))        