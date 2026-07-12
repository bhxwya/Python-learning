students_dict = {
"Student1": [85, 90, 78, 92, 88],
"Student2": [75, 88, 92, 80, 87],
"Student3": [90, 95, 89, 78, 93],
"Student4": [80, 85, 88, 92, 87],
"Student5": [92, 88, 95, 90, 85],
}

for key,value in students_dict.items():
    total = 0
    for i in value:
        total = total + i
    percentage = total/len(value)
    print(f"{key} -> Sum: {total}, Percentage: {percentage}")
        
    
    
