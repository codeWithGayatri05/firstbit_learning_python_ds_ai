class Employee:
    def __init__(self, id, name, salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    # Getter methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    # Setter methods
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    # Behaviour
    def display(self):
        print("ID =", self.__id)
        print("Name =", self.__name)
        print("Salary =", self.__salary)


e1 = Employee(1, "Sachin", 50000)

e1.display()

print("Salary =", e1.get_salary())

e1.set_salary(60000)

e1.display()