def total_marks(physics, maths, science, english, hindi):
    print(f"Your marks in physics = {physics}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in science = {science}")
    print(f"Your marks in english = {english}")
    print(f"Your marks in hindi = {hindi}")
    total = physics + maths + science + english + hindi
    print(f"Your total marks = {total}")


# total_marks(20, 98, science=34, 34, 34)  # error

# total_marks(20, 98, science=34, hindi=23, english=98)  # works

# total_marks(physics=23,45,56,45,34)  #error

total_marks(39,98,76,34,hindi=78)  #works

# total_marks(98,34,5,5,23) #works


