students_data = {
    "anirudh": {
        "roll_number": 101,
        "gender": "Male",
        "marks": {"physics": 78, "maths": 89, "chemistry": 67},
    },
    "sara": {
        "roll_number": 102,
        "gender": "Female",
        "marks": {"physics": 90, "maths": 75, "chemistry": 82},
    },
    "alex": {
        "roll_number": 103,
        "gender": "Male",
        "marks": {"physics": 82, "maths": 91, "chemistry": 56},
    },
}
for students_name,details in students_data.items():
    total_marks = sum(details["marks"].values())
    print(f"{students_name} -> {total_marks/len(details["marks"]):.2f}%")