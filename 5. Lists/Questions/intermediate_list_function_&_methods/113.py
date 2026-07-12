my_marks = [7.2, 7.14, 6.71, 7.14, 7.3]
Total = 0


for i in my_marks:
    Total = Total + i

average = Total/len(my_marks)
print(f"Average of your list is {average:.2f}")
