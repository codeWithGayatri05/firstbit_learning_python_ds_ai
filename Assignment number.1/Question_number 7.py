days = int(input("Enter number of days:"))
years = days//365
remanining_days = days%365
weeks = remanining_days//7
days_left = remanining_days%7
print("years:",years)
print("weeks:",weeks)
print("days:",days_left)