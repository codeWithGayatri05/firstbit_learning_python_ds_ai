class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
m1 = Mobile("Apple", "iPhone 13", 90900)
m2 = Mobile("Samsung", "Galaxy S21", 79900)

m1.display_info()
m2.display_info()