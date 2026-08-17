"""
==============================
WHY DO WE USE OOP?
==============================

Without OOP:
• Data is stored in lists or dictionaries.
• Difficult to manage large programs.
• Hard to update information.

With OOP:
• Data and functions stay together.
• Easy to organize code.
• Easy to reuse and maintain.
"""

# Student records using List

student1 = ["Madhav", 10]
student2 = ["Vishakha", 12]

student1.append("A")

print(student1)
print(f"{student1[0]} is in class {student1[1]}")
print(f"{student2[0]} is in class {student2[1]}")