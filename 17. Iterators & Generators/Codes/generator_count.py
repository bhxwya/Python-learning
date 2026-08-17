# ============================================================
# GENERATOR EXAMPLE 1: COUNT TO A NUMBER
# ============================================================

def count_to(n):

    count = 1

    while count <= n:

        # yield gives the current value and pauses the generator.
        yield count

        # The generator resumes here when the next value is requested.
        count += 1


number = int(input("Enter a number to count up to: "))

for n in count_to(number):
    print(n)


# ============================================================
# HOW IT WORKS
# ============================================================

# If the user enters 3:
#
# count = 1
#     ↓
# yield 1 → pause
#
# resume
#     ↓
# count = 2
#     ↓
# yield 2 → pause
#
# resume
#     ↓
# count = 3
#     ↓
# yield 3 → pause
#
# resume
#     ↓
# count = 4
#     ↓
# 4 <= 3 is False
#     ↓
# generator ends