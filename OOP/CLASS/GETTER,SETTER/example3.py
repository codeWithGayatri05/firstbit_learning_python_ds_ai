class Bank:
    def __init__(self, accno, name, balance):
        self.__accno = accno
        self.__name = name
        self.__balance = balance

    # Getter methods
    def get_accno(self):
        return self.__accno

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    # Setter methods
    def set_accno(self, accno):
        self.__accno = accno

    def set_name(self, name):
        self.__name = name

    def set_balance(self, balance):
        self.__balance = balance

    # Behaviour
    def display(self):
        print("Account No =", self.__accno)
        print("Name =", self.__name)
        print("Balance =", self.__balance)


b1 = Bank(101, "Vijay", 25000)

b1.display()

print("Balance =", b1.get_balance())

b1.set_balance(35000)

b1.display()