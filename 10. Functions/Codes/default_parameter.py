def total_marks(physics=0, maths=0, science=0, english=0, hindi=0):
    print(f"Your marks in physics = {physics}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in science = {science}")
    print(f"Your marks in english = {english}")
    print(f"Your marks in hindi = {hindi}")
    total = physics + maths + science + english + hindi
    print(f"Your total marks = {total}")


# total_marks(23, 45)  # works

# total_marks(english=23, physics=45)  # works

# total_marks()  # works

