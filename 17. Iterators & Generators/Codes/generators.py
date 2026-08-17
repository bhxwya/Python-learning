# ============================================================
# GENERATORS
# ============================================================

# A generator is a function that behaves like an iterator.
# It produces values one at a time and can be used in a for loop.
#
# Generators use 'yield' instead of 'return'.


# ============================================================
# return vs yield
# ============================================================

# return:
# - Gives a value back from a function.
# - Immediately ends the function.
#
# yield:
# - Gives a value from a generator.
# - Pauses the generator.
# - It can resume from where it paused later.


# Example of return:

def normal_function():
    return 10


result = normal_function()
print(result)


# Example of yield:

def generator_function():
    yield 10
    yield 20
    yield 30


for number in generator_function():
    print(number)


# ============================================================
# RETURN vs YIELD
# ============================================================

# return:
#
# return value
#     ↓
# gives value
#     ↓
# function ends


# yield:
#
# yield value
#     ↓
# gives value
#     ↓
# function pauses
#     ↓
# resumes later
#     ↓
# next yield


# Easy way to remember:
#
# return = pouring a bucket
# yield  = drip faucet


# ============================================================
# GENERATORS AND ITERATORS
# ============================================================

# A generator behaves like an iterator.
#
# With a custom iterator, we manually write:
#
# __iter__()
# __next__()
# StopIteration
#
# With a generator, Python handles this iterator machinery
# for us.


# Custom Iterator:
#
# class Example:
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         ...
#
#         raise StopIteration


# Generator:
#
# def example():
#     yield value


# ============================================================
# ADVANTAGE OF GENERATORS
# ============================================================

# Generators produce values one at a time.
# They do not need to store all values in memory at once.
#
# This is especially useful when working with large amounts
# of data, such as large files.