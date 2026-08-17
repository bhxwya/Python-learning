# ============================================================
# LAMBDA FUNCTIONS
# ============================================================

# Functional Python:
#
# Functional programming is a programming style where
# functions are used as the main building blocks to
# process and transform data.
#
# Python provides tools such as lambda, map(), filter()
# and reduce() to make functional-style programming easier.


# ============================================================
# WHAT IS A LAMBDA FUNCTION?
# ============================================================

# A lambda function is a small anonymous function.
# "Anonymous" means it does not have a normal function name.
#
# Syntax:
#
# lambda arguments: expression


# Normal function:

def double(x):
    return x * 2

print(double(5))


# Same thing using lambda:

double = lambda x: x * 2

print(double(5))


# Lambda with multiple arguments:

multiply = lambda x, y: x * y

print(multiply(4, 5))


# Another example:

average = lambda x, y, z: (x + y + z) / 3

print(average(3, 5, 10))


# ============================================================
# IMPORTANT
# ============================================================

# Lambda functions are generally used for small, simple
# operations, especially when a function is needed temporarily.
#
# Lambda functions contain a single expression.