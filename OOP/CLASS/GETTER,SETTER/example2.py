class Mobile:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price

    # Getter methods
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    # Setter methods
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__price = price

    # Behaviour
    def display(self):
        print("Brand =", self.__brand)
        print("Model =", self.__model)
        print("Price =", self.__price)


m1 = Mobile("Samsung", "S24", 70000)

m1.display()

print("Price =", m1.get_price())

m1.set_price(65000)

m1.display()