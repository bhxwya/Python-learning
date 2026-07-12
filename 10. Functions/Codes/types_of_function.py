
"""
NOTE:
These 4 types are not official Python function categories.
They are created by Code and Debug only for easier concept understanding.

Functions can be understood based on two things:

1. Parameter → Does the function receive input?
2. Return    → Does the function send a value back?
"""


# ------------------------------------------------------------
# 1. WITHOUT PARAMETER, WITHOUT RETURN
# ------------------------------------------------------------

# Takes no input and returns no value.
# It only performs a task.

def greet():
    print("Hello")


greet()

# Flow:
# Nothing goes in → Function works → Nothing comes back


# ------------------------------------------------------------
# 2. WITH PARAMETER, WITHOUT RETURN
# ------------------------------------------------------------

# Takes input through a parameter but returns no value.
# It uses the given value to perform a task.

def greet_user(name):
    print(f"Hello {name}")


greet_user("Ansh")

# Here:
# name = parameter
# "Ansh" = argument
#
# Flow:
# "Ansh" goes in → Function works → Nothing comes back


# ------------------------------------------------------------
# 3. WITHOUT PARAMETER, WITH RETURN
# ------------------------------------------------------------

# Takes no input but returns a value.

def get_number():
    return 100


num = get_number()
print(num)

# Here:
# The function returns 100.
# The returned value is stored in num.
#
# Flow:
# Nothing goes in → Function works → 100 comes back


# ------------------------------------------------------------
# 4. WITH PARAMETER, WITH RETURN
# ------------------------------------------------------------

# Takes input through parameters and returns a value.

def add(num1, num2):
    return num1 + num2


result = add(10, 20)
print(result)

# Here:
# num1 and num2 = parameters
# 10 and 20 = arguments
# The returned value (30) is stored in result.
#
# Flow:
# 10 and 20 go in → Function works → 30 comes back


"""
QUICK SUMMARY:

Parameter = Value going INTO the function.
Return    = Value coming OUT OF the function.

1. No Parameter + No Return → No input, no output
2. Parameter + No Return    → Input, no output
3. No Parameter + Return    → No input, output
4. Parameter + Return       → Input and output
"""