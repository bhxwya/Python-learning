students_data = {
    "Student1": [85, 90, 78, 92, 88],
    "Student2": [75, 88, 92, 80, 99],
    "Student3": [90, 95, 89, 99, 93],
    "Student4": [80, 85, 88, 92, 87],
    "Student5": [92, 88, 95, 90, 85],
}

highest_marks = 0
highest_scorrer = ""
for key, value in students_data.items():
    total = 0
    for i in value:
        total = total + i

    if highest_marks < total:
        highest_marks = total
        highest_scorrer = key
        
    
print(f"Student with the highest marks: {highest_scorrer}")