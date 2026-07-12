marks1 = int(input("Enter your Chemistry marks:"))
max_marks1 = int(input("Enter maximum marks for the Chemistry subject:"))
marks2 = int(input("Enter your Physics marks:"))
max_marks2 = int(input("Enter maximum marks for the Physics subject:"))
marks3 = int(input("Enter your Maths marks:"))
max_marks3 = int(input("Enter maximum marks for the Maths subject:"))
marks4 = int(input("Enter your English marks:"))
max_marks4 = int(input("Enter maximum marks for the English subject:"))
marks5 = int(input("Enter your Social Studies marks:"))
max_marks5 = int(input("Enter maximum marks for the Social Studies subject:"))


percentage = ((marks1+marks2+marks3+marks4+marks5) /
              (max_marks1+max_marks2+max_marks3+max_marks4+max_marks5))*100

print(f"Your percentage is {percentage:.2f}")

if percentage > 100:
    print("Invalid marks entered")

elif percentage >= 90:
    print("GRADE A")

elif percentage >= 80:
    print("GRADE B")

elif percentage >= 70:
    print("GRADE C")

elif percentage >= 60:
    print("GRADE D")

else:
    print("FAIL")