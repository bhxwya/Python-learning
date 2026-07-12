students_data = {
    "anirudh": {
        "roll_number": 101,
        "gender": "Male",
        "marks": [78, 89, 67, 92, 54],
    },

    "sara": {
        "roll_number": 202,
        "gender": "Female",
        "marks": [90, 75, 82, 68, 91],
    },

    "alex": {
        "roll_number": 303,
        "gender": "Female",
        "marks": [82, 91, 56, 78, 69],
    }
}

for students_name,details in students_data.items():
    total = 0
    for mark in details["marks"]:
         total = total + mark
    print(f"{students_name} -> Total Marks: {total}")