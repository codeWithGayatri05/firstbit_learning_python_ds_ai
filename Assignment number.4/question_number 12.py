num = int(input("Enter a number to check if Armstrong: "))
num_str = str(num)
num_digits = len(num_str)
total_sum = 0

for digit in num_str:
    total_sum += int(digit) ** num_digits

if total_sum == num:
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")