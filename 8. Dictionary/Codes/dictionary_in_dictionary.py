students_data = {
    "anirudh": {
        "roll_number": 431,
        "gender": "Male",
        "physics": 78,
        "chemistry": 89,
        "maths": 67,
    },
    "sanjay": {
        "roll_number": 122,
        "gender": "Female",
        "physics": 90,
        "chemistry": 75,
        "maths": 82,
    },
    "raj": {
        "roll_number": 786,
        "gender": "Female",
        "physics": 82,
        "chemistry": 91,
        "maths": 56,
    }
}

for name, details in students_data.items():
    print(
        f"{name} -> Total marks: {details["physics"]+details["chemistry"]+details["maths"]}")

print(type(students_data["anirudh"]["chemistry"]))
print(type(students_data["anirudh"]))
print(type(students_data))