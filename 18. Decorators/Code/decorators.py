# ============================================================
# DECORATORS
# ============================================================

# A decorator is a function that extends the behavior of
# another function without modifying the original function.
#
# A decorator takes a function as an argument, wraps it with
# extra behavior, and returns the wrapped function.


# ============================================================
# BASIC DECORATOR
# ============================================================

def add_sprinkles(func):

    # wrapper is just the name of the inner function.
    # It is NOT a mandatory Python keyword.
    #
    # The wrapper receives the arguments of the original
    # function and passes them to it.

    def wrapper(*args, **kwargs):

        # Extra behavior added by the decorator.
        print("Sprinkles 🎊")

        # Call the original function.
        # *args and **kwargs pass the original arguments
        # to the original function.
        func(*args, **kwargs)

    # Return the wrapper function.
    return wrapper


# ============================================================
# UNDERSTANDING *args AND **kwargs
# ============================================================

# *args
# → collects positional arguments into a tuple.
#
# Example:
#
# get_ice_cream("vanilla")
#
# args = ("vanilla",)


# **kwargs
# → collects keyword arguments into a dictionary.
#
# Example:
#
# get_ice_cream(flavor="vanilla", size="large")
#
# kwargs = {
#     "flavor": "vanilla",
#     "size": "large"
# }


# When calling the original function:
#
# func(*args, **kwargs)
#
# *args and **kwargs unpack the arguments and pass them
# to the original function.


# ============================================================
# WITHOUT @ SYNTAX
# ============================================================

# A decorator can be used without the @ symbol.

def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")


get_ice_cream = add_sprinkles(get_ice_cream)

get_ice_cream("vanilla")


# ============================================================
# USING @ DECORATOR SYNTAX
# ============================================================

# @add_sprinkles is shorthand for:
#
# get_ice_cream = add_sprinkles(get_ice_cream)


@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")


get_ice_cream("vanilla")


# ============================================================
# HOW THE DECORATOR WORKS
# ============================================================

# Original function:
#
# get_ice_cream("vanilla")
#
#        ↓
#
# wrapper("vanilla")
#
#        ↓
#
# print("Sprinkles 🎊")
#
#        ↓
#
# func(*args, **kwargs)
#
#        ↓
#
# get_ice_cream("vanilla")
#
#        ↓
#
# Here is your vanilla ice cream 🍨


# ============================================================
# MULTIPLE DECORATORS
# ============================================================

def add_fudge(func):

    def wrapper(*args, **kwargs):
        print("Fudge 🍫")
        func(*args, **kwargs)

    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")


get_ice_cream("vanilla")


# ============================================================
# ORDER OF MULTIPLE DECORATORS
# ============================================================

# Decorators are applied from BOTTOM to TOP.
#
# This:
#
# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     ...
#
# is approximately:
#
# get_ice_cream = add_sprinkles(
#                     add_fudge(
#                         get_ice_cream
#                     )
#                 )


# Therefore the execution order is:
#
# add_sprinkles
#       ↓
# add_fudge
#       ↓
# original get_ice_cream()


# Output:
#
# Sprinkles 🎊
# Fudge 🍫
# Here is your vanilla ice cream 🍨


# ============================================================
# QUICK REVISION
# ============================================================

# Decorator
# → extends a function's behavior without modifying it.


# func
# → represents the original function passed to the decorator.


# wrapper
# → inner function that adds extra behavior and calls func.


# *args
# → collects positional arguments.


# **kwargs
# → collects keyword arguments.


# func(*args, **kwargs)
# → calls the original function and passes its arguments.


# return wrapper
# → returns the new wrapped function.


# @decorator
# → shorthand for:
#   function = decorator(function)
