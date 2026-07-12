"""
Write a Python program to check if two given sets have no elements
in common.
"""

set1 = {5, 6, 2, 1, "Anirudh", 7, 76}
set2 ={"Python", 76, 22, 91, -991}

if set1 & set2 == set():
    print("No elements in common")
else:
    print(f"has common elements: {set1 & set2}")