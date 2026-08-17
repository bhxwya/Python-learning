# ============================================================
# filter()
# ============================================================

# filter() selects elements from an iterable based on a
# condition.
#
# Syntax:
#
# filter(function, iterable)
#
# The function should return True or False.


# ============================================================
# EXAMPLE: EVEN NUMBERS
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]


# Using a normal loop:

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)


# ============================================================
# USING filter()
# ============================================================

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))


# ============================================================
# ANOTHER EXAMPLE
# ============================================================

numbers = [1, 2, 4, 6, 8, 3]

result = filter(lambda x: x > 2, numbers)

print(list(result))


# ============================================================
# HOW filter() WORKS
# ============================================================

# [1, 2, 3, 4, 5, 6]
#
# lambda x: x % 2 == 0
#
# 1 → False → removed
# 2 → True  → kept
# 3 → False → removed
# 4 → True  → kept
# 5 → False → removed
# 6 → True  → kept
#
# Result:
#
# [2, 4, 6]


# ============================================================
# IMPORTANT
# ============================================================

# filter() does NOT transform every item.
# It selects/keeps items that satisfy a condition.
#
# Main purpose:
#
# filter() → select items.