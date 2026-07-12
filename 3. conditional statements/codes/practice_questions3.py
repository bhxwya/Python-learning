"""34"""
classes_held = int(input("Enter the number of classes held:"))
classes_attented = int(input("Enter the number of classes you attented:"))

attendance_percentage = (classes_attented/classes_held)*100
print(f"You attendance percentage is {attendance_percentage:.1f}")

if attendance_percentage >= 75:
    print("Allowed to sit in examination")

else:
    print ("Not allowed to sit in the exmination")

"""35"""
salary = int(input("Enter your salary: Rs."))

if salary < 10000:
    print("Your salary is incremented by 5% ")
    updated_salary = (salary * 5)/100 + salary
    print(f"Now, your salary is Rs.{updated_salary}")
elif salary <= 20000:
    print("Your salary is incremented by 10% ")
    updated_salary = (salary * 10)/100 + salary
    print(f"Now, your salary is Rs.{updated_salary}")
elif salary <= 50000:
    print("Your salary is incremented by 15% ")
    updated_salary = (salary * 15)/100 + salary
    print(f"Now, your salary is Rs.{updated_salary}")

else:
    print("Your salary is incremented by 20% ")
    updated_salary = (salary * 20)/100 + salary
    print(f"Now, your salary is Rs.{updated_salary}")

"""36"""
num1 = float(input("Enter your fisrt number:"))
num2 = float(input("Enter your second number:"))
num3 = float(input("Enter your third number:"))

if num1 == num2 == num3:
    print("Equal Numbers")

elif num1 >= num2 and num1 >= num3:
    print(f"Number first {num1} is the greatest")

elif num2 >= num1 and num2 >= num3:
    print(f"Number second {num2} is the greatest")

else:
    print(f"Number third {num3} is the greatest")

"""37"""
year = int(input("Enter a year to check if it is a leap or not:"))

if year % 4 == 0 and year % 400 == 0:
    print(f"Year {year} is a leap year")

elif year % 4 == 0 and year % 100 == 0:
    print("Not a leap year")

elif year % 4 == 0:
    print(f"Year {year} is a leap year")

else:
    print("Not a leap year")
