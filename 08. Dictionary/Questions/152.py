employees = {
    "rahul": {
        "department": "IT",
        "salary": 55000,
        "skills": {"python": 8, "sql": 7, "javascript": 6},
    },
    "priya": {
        "department": "HR",
        "salary": 48000,
        "skills": {"communication": 9, "recruitment": 8, "excel": 7},
    },
    "arjun": {
        "department": "IT",
        "salary": 62000,
        "skills": {"python": 9, "sql": 8, "javascript": 7},
    },
}

highest_skills_score = 0
highest_skills_scorrer = ""
for employees_name,employees_details in employees.items():
    skills_score = (sum(employees_details["skills"].values()))
    if skills_score>highest_skills_score:
        highest_skills_score = skills_score
        highest_skills_scorrer = employees_name
        
    
print(f"Employee with highest skill score: {highest_skills_scorrer} \n Total skill score: {highest_skills_score}")
    