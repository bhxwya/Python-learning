"""23"""
num = int(
    input("Enter a number to find whether it is a positive number or negative :"))

if num >= 0:
    print("Positive Number")

else:
    print("Negative Number")

"""24"""
char = input(
    "Enter a character to find whether it is a consonant or vowel :").lower()

if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print("vowel")

else:
    print("consonant")


"""25"""
num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))

if num1 % num2 == 0:
    print("It is Divisible")

else:
    print("Not ")


"""26"""
classes_held = int(input("Total number of classes held:"))
classes_attented = int(input("Total number of classes attented:"))

attendance = classes_attented/classes_held * 100
print(f"Your attendance percentage is {attendance:.2f}%")

if attendance >= 75:
    print("You are allowed to sit in exam")

else:
    print("You are not allowed to sit in exam")
