class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    # Getter methods
    def get_length(self):
        return self.__length

    def get_breadth(self):
        return self.__breadth

    # Setter methods
    def set_length(self, length):
        self.__length = length

    def set_breadth(self, breadth):
        self.__breadth = breadth

    # Behaviour
    def area(self):
        return self.__length * self.__breadth

    def display(self):
        print("Length =", self.__length)
        print("Breadth =", self.__breadth)
        print("Area =", self.area())


r1 = Rectangle(10, 5)

r1.display()

print("Length =", r1.get_length())

r1.set_length(20)

r1.display()