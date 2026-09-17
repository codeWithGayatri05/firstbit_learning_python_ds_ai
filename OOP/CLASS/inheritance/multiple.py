class A:
    def add(self):
        print("add a")


class B:
    def add(self):
        print("add b")

class C(B,A):
    def add(self):
        print("add C")

c1 = C()
c1.add()
    
