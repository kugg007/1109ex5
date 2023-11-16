import math

class MyShape:
    def __init__(self,side,length,width,radius):
        self.side = side
        self.length = length
        self.width = width
        self.radius = radius

    def square_area(self):
        print(self.side*self.side)
    def rectangle_area(self):
        print(self.length*self.width)
    def circular_area(self):
        print(self.radius*self.radius*math.pi)

ms = MyShape(5,2,5,10)
ms.square_area()
ms.rectangle_area()
ms.circular_area()