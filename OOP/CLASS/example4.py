class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of rectangle:", self.length * self.breadth)

r1 = Rectangle(10, 20)
r2 = Rectangle(15, 25)

r1.area()
r2.area()