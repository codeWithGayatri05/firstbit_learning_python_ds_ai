class student:
    def __init__(self, roll_no,Name ,Marks):
        self.roll_no = roll_no
        self.name = Name
        self.marks = Marks

    def display(self):
        print("Roll No :", self.roll_no)
        print("Name :", self.name)
        print("Marks :", self.marks)

S1= student(101, "Sanket", 85)
S2= student(102, "Rohit", 90)
S1.display()
S2.display()