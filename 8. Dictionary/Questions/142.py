marks = {}
subject_count = int(input("Enter the numbers of subject: "))
# total_marks = 0
for _ in range(0, subject_count):
    subject_name = (input("Enter the subject name: "))
    subject_marks = float(input(f"Enter the marks for {subject_name}: "))
    marks.update({subject_name: subject_marks})
    # marks[subject_name] = subject_marks
    # total_marks = total_marks + subject_marks
print(marks)
# print(f"Your percentage is {(total_marks/(subject_count*100)*100)}")
