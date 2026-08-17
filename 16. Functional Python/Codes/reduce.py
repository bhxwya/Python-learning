# ============================================================
# reduce()
# ============================================================

# reduce() repeatedly applies a function to the elements
# of an iterable and combines them into a single final value.
#
# reduce() is available from the functools module.
#
# Syntax:
#
# reduce(function, iterable)


from functools import reduce


# ============================================================
# EXAMPLE: SUM OF NUMBERS
# ============================================================

numbers = [1, 2, 3, 4, 5]


# Using a normal loop:

total = 0

for number in numbers:
    total = total + number

print(total)


# ============================================================
# USING reduce()
# ============================================================

total = reduce(lambda x, y: x + y, numbers)

print(total)


# ============================================================
# HOW reduce() WORKS
# ============================================================

# numbers = [1, 2, 3, 4, 5]
#
# First:
# 1 + 2 = 3
#
# Then:
# 3 + 3 = 6
#
# Then:
# 6 + 4 = 10
#
# Then:
# 10 + 5 = 15
#
# Final result:
# 15


# ============================================================
# USING A NORMAL FUNCTION
# ============================================================

def my_sum(x, y):
    return x + y


numbers = [1, 2, 3, 4, 5]

total = reduce(my_sum, numbers)

print(total)


# ============================================================
# IMPORTANT
# ============================================================

# reduce() combines multiple values into ONE final value.
#
# Main purpose:
#
# reduce() → combine items into one result.