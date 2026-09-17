# Q.create class distance with data members as km,m and cm and add following methods
# constructor
# destructor
# overload +,- operator


class Distance:
    # Constructor
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    # Destructor
    def __del__(self):
        print("Object destroyed")

    # Overload + operator
    def __add__(self, other):
        cm = self.cm + other.cm
        m = self.m + other.m
        km = self.km + other.km

        if cm >= 100:
            m += cm // 100
            cm = cm % 100

        if m >= 1000:
            km += m // 1000
            m = m % 1000

        return Distance(km, m, cm)

    # Overload - operator
    def __sub__(self, other):
        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = other.km * 100000 + other.m * 100 + other.cm

        total = total1 - total2

        km = total // 100000
        total = total % 100000

        m = total // 100
        cm = total % 100

        return Distance(km, m, cm)

    
    def display(self):
        print(self.km, "km", self.m, "m", self.cm, "cm")



d1 = Distance(5, 600, 50)
d2 = Distance(2, 500, 75)

print("Distance 1:")
d1.display()

print("Distance 2:")
d2.display()

# Addition
d3 = d1 + d2
print("Addition:")
d3.display()

# Subtraction
d4 = d1 - d2
print("Subtraction:")
d4.display()