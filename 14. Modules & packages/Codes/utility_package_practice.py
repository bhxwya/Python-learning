# ============================================================
# BEFORE: Importing the modules
# ============================================================

# We import the modules from the package.
# Then we access their functions using module.function().
# __init__.py was empty.

# from my_utils import calculator, string_utils


# print(calculator.add(10, 20))
# print(calculator.subtract(20, 5))
# print(calculator.multiply(5, 4))

# print(string_utils.uppercase("hello"))
# print(string_utils.lowercase("PYTHON"))
# print(string_utils.reverse("Ansh"))


# ============================================================
# AFTER: Using __init__.py
# ============================================================

# __init__.py imports and exposes the functions from the modules.
# Now we can import the functions directly from my_utils.
# We no longer need calculator.function() or string_utils.function().

from my_utils import add, subtract, multiply
from my_utils import uppercase, lowercase, reverse


print(add(10, 20))
print(subtract(20, 5))
print(multiply(5, 4))

print(uppercase("hello"))
print(lowercase("PYTHON"))
print(reverse("Ansh"))