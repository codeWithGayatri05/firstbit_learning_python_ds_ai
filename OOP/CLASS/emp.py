class Employee:
    def __init__(self, eid, ename, esal):
        self.id = eid
        self.name = ename
        self.sal = esal

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tSal={self.sal}")


e1 = Employee(12, "Sachin", 9087)
e2 = Employee(18, "Smriti", 38383)

# e1.display()
# e2.display()

print(e1.sal)
print(e2.name)

e1.name = "Virat"
print("e1")