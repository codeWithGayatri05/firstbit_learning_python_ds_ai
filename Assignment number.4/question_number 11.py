num = int(input("Enter a number to check if strong: "))
temp = num
total_sum = 0

while temp > 0:
    digit = temp % 10
    
    
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
        
    total_sum += fact
    temp //= 10

if total_sum == num:
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is not a Strong Number.")