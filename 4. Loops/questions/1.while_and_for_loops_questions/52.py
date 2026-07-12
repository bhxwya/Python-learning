num = int(input("Enter a no. you want to find factorial of:"))

factorial = 1
x = 1

while x <= num:
    factorial = factorial * x
    x += 1
print(factorial)