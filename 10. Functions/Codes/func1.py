# ==================== LOCAL & GLOBAL VARIABLES ====================

# GLOBAL VARIABLES:
# Variables created outside all functions are called global variables.
# They can be accessed from anywhere in the program.

num1 = 100
num2 = 100


def add():

    # LOCAL VARIABLES:
    # Variables created inside a function are called local variables.
    # They can only be accessed inside that function.

    num1 = int(input("Enter num1 = "))
    num2 = int(input("Enter num2 = "))

    print(f"Sum = {num1 + num2}")


add()

# These print statements use the GLOBAL num1 and num2.
# The local variables inside add() do not change these global variables.

print(num1)
print(num2)


# ==================== SCOPE ====================

# Scope means:
# "The area of a program where a variable can be accessed."

# 1. Local Scope:
#    A variable created inside a function belongs to that function.
#    It cannot normally be accessed outside the function.

# 2. Global Scope:
#    A variable created outside all functions belongs to the global scope.
#    It can be accessed throughout the program.

# IMPORTANT:
# A local variable and a global variable can have the same name.
# Python treats them as different variables because they belong
# to different scopes.