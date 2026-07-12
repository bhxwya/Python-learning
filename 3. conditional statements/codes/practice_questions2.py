"""27"""
num = int(input("Enter a number to find whether a number is odd or even:"))

if num == 0:
    print("Number is equal to zero")

elif num % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")


"""28"""
num = int(input(
    "Enter a number to find whether a number is divisible by 2 and 3 but not 8:"))

if (num % 2 != 0):
    print("Not Divisble by 2 ")

elif num % 3 != 0:
    print("Not Divisble by 3")

elif num % 8 == 0:
    print("Divisble by 8")

else:
    print("Valid number")


"""29"""
num = int(input("Enter a number to print the last digit of it:"))
num = num % 10
print(f"Last digit of your input no. is {num}")


"""30"""
num = int(input(
    "Enter a number to check whether the last digit of your num is divisble by 5 or not:"))
x = num % 10

if x % 5 == 0:
    print(f"Yes, the last digit {x} is divisible by 5")

else:
    print(f"No, the last digit {x} is not divisible by 5")


"""31"""
final_amount = int(input("Enter the final amount: Rs."))
if final_amount >= 50000:
    print("Congratulations, You get a 30% Discount")
    after_discount = final_amount - (final_amount*30/100)
    print(f"Your final price is Rs. {after_discount}")

elif final_amount >= 40000:
    print("Congratulations, You get a 25% Discount")
    after_discount = final_amount - (final_amount*25/100)
    print(f"Your final price is Rs. {after_discount}")

elif final_amount >= 30000:
    print("Congratulations, You get a 20% Discount")
    after_discount = final_amount - (final_amount*20/100)
    print(f"Your final price is Rs. {after_discount}")

elif final_amount >= 10000:
    print("Congratulations, You get a 10% Discount")
    after_discount = final_amount - (final_amount*10/100)
    print(f"Your final price is Rs. {after_discount}")

elif final_amount >= 1:
    print("Sorry, No discount availaible on this amount")
    after_discount = final_amount
    print(f"Your final price is Rs. {after_discount}")

else:
    print("You haven't bought anything")

"""32"""
print("This program helps you find the smallest number for different-different number")
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))
num3 = float(input("Enter your third number:"))
num4 = float(input("Enter your fourth number:"))

if (num1 == num2 or
    num1 == num3 or
    num1 == num4 or
    num2 == num3 or
    num2 == num4 or
    num3 == num4):
    print("Numbers aren't different")

elif num1 < num2 and num1 < num3 and num1 < num4:
    print(f"First number {num1} is the smallest")

elif num2 < num1 and num2 < num3 and num2 < num4:
    print(f"Second number {num2} is the smallest")

elif num3 < num1 and num3 < num2 and num3 < num4:
    print(f"Third number {num3} is the smallest")


else:
    print(f"Fourth number {num4} is the smallest")

"""33"""
num = int(input("Enter a number:"))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

elif num % 3 == 0:
    print("Fizz")

elif num % 5 == 0:
    print("Buzz")

else:
    print(f"{num}")
