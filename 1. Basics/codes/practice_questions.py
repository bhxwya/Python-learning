4.
num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))

total = num1 + num2

print(f"Your total is = {total}")

5.
age = "20"
x = 3

sum = int(age)+x
print(sum)

umar = 20
y = "3"

whatever = str(umar)+y
print(whatever)

6.
length = float(input("Enter the length of rectange = "))
width = float(input("Enter the width = "))

area = length * width
print(f"Area of rectangle is = {area}")


7.
age = 20.8
x = 3

sum = int(age)+x
print(sum)

umar = 20
y = 3.9

whatever = float(umar)+y
print(whatever)


8.
num1 = float(input("Enter first number = "))
num2 = float(input("Enter second number = "))
num3 = float(input("Enter third number = "))

average = (num1+num2+num3)/3
print(f"Your average is = {average}")


9.
fahrenheit = float(input("Enter the fahrenheit temperature = "))
celsius = (fahrenheit-32)*5/9

print(f"Your temperature in celsius is = {celsius:.2f}")


10.
marks1 = float(input("Enter English number = "))
marks2 = float(input("Enter Maths number = "))
marks3 = float(input("Enter Hindi number = "))
marks4 = float(input("Enter Science number = "))
marks5 = float(input("Enter Social studies number = "))
total_marks = float(input("Enter total maximum marks = ="))

percentage = ((marks1+marks2+marks3+marks4+marks5)/total_marks)*100
print(f"Your percentage is = {percentage}")


11.
total_games = int(input("Enter total no. of games played = "))
total_wins = int(input("Enter total no. of wins = "))
total_losses = int(input("Enter total no. of losses = "))

winning_points = total_wins*4
tie_games = (total_games)-(total_wins+total_losses)
tie_points = tie_games*2

total_points = winning_points+tie_points

print(f"Total tie games = {tie_games}")
print(f"Total points = {total_points}")
