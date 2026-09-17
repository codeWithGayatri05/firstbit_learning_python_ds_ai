class Bank:
    def __init__(self, accno, name, balance):
        self.accno = accno
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        print("account number:", self.accno)
        print("account holder name:", self.name)
        print("balance:", self.balance)

    b1 = Bank(101, "Sanket", 10000)
    b2 = Bank(102, "Rohit", 20000)

    b1.display()
    b2.display()


    