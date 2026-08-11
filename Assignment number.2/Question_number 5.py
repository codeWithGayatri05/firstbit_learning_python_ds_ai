print("calculate selling price of Book")
cost_price = float(input("Enter cost price of Book:"))
discount = float(input("Enter discount(%):"))
discount_amount =(cost_price*discount)/100
selling_price =(cost_price-discount_amount)
print(f"discount amount :{discount_amount}.")
print(f"selling_price of book: {selling_price}.")