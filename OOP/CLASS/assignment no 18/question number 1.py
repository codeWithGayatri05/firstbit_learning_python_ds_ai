class ComplexNumber:

    # Constructor
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Overload + operator
    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    # Overload - operator
    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    # Display complex number
    def display(self):
        print(self.real, "+", self.imaginary, "i")

    # Destructor
    def __del__(self):
        print("Object destroyed")


# Create objects
c1 = ComplexNumber(10, 20)
c2 = ComplexNumber(5, 10)

print("First Complex Number:")
c1.display()

print("Second Complex Number:")
c2.display()

# Addition
c3 = c1 + c2
print("Addition:")
c3.display()

# Subtraction
c4 = c1 - c2
print("Subtraction:")
c4.display()