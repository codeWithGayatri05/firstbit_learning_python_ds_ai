class emp():
    def calsal(self):
        print("emp salary")


class Hr(emp):
    pass
    # def calsal(self):
    #     print("Hr current salary")

class admin (emp):
    pass
    # def calsal(self):
    #     print("admin salary")

h = Hr()
a = admin()

h.calsal()
a.calsal()    
