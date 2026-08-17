# ============================================================
# map()
# ============================================================

# map() applies a function to every item in an iterable.
#
# Syntax:
#
# map(function, iterable)
#
# It is commonly used to transform every element.


# ============================================================
# EXAMPLE
# ============================================================

numbers = [1, 2, 3, 4, 5]


# Normal approach using a loop:

doubled = []

for number in numbers:
    doubled.append(number * 2)

print(doubled)


# ============================================================
# USING map()
# ============================================================

# lambda x: x * 2
# means: take x and return x * 2.
#
# map() applies this function to every number.

doubled = map(lambda x: x * 2, numbers)

print(list(doubled))


# ============================================================
# USING A NORMAL FUNCTION WITH map()
# ============================================================

def cube(x):
    return x * x * x


numbers = [1, 2, 3, 4, 5]

cubed = map(cube, numbers)

print(list(cubed))


# ============================================================
# IMPORTANT
# ============================================================

# map() returns a map object (an iterator).
# We commonly use list() to convert the result into a list.
#
# Main purpose:
#
# map() → transform every item.