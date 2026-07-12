subject_marks_dict = {
"Math": 90,
"English": 85,
"Science": 92,
"History": 88,
"Computer Science": 95
}

subject_name = input("Enter a subject name: ")

marks = subject_marks_dict.get(subject_name)

if marks is None:
    print("Invalid")
else:
    print(marks)
