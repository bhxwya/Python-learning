# ============================================================
# ITERATORS
# ============================================================

# An iterator is an object that returns elements one at a time
# and remembers its current position between calls.
#
# An iterator uses two special (dunder) methods:
#
# __iter__() -> returns the iterator object
# __next__() -> returns the next item
#
# When there are no more items, __next__() raises StopIteration.


# ============================================================
# DUNDER METHODS
# ============================================================

# Dunder means "double underscore".
#
# They are special methods that Python calls automatically
# when certain operations are performed.
#
# Examples:
#
# __init__()  -> called when an object is created
# __str__()   -> called when an object is converted to a string
# __iter__()  -> called when iter() is used
# __next__()  -> called when next() is used


# ============================================================
# CREATING A CUSTOM ITERATOR
# ============================================================

import random


class Dice:

    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0

    # __iter__() returns the iterator object.
    # Here, the Dice object itself is the iterator.

    def __iter__(self):
        return self

    # __next__() provides the next value.
    # count keeps track of how many values were produced.

    def __next__(self):

        if self.count < self.rolls:

            self.count += 1

            return random.randint(1, 6)

        else:

            # StopIteration tells Python that there
            # are no more values.

            raise StopIteration


# Create an iterator that can produce 3 dice rolls.

dice = Dice(3)


# The for loop automatically uses iter() and next()
# to get values from the iterator.

for die in dice:
    print(die)


# ============================================================
# HOW THE FOR LOOP WORKS INTERNALLY
# ============================================================

# The following code is a conceptual representation of
# what the for loop is doing with an iterator.
#
# It is commented out because the iterator above has already
# been exhausted by the for loop.

# iterator = Dice(3)
# iterator = iter(dice)

# while True:
#     try:
#         die = next(iterator)
#         print(die)
#
#     except StopIteration:
#         break


# ============================================================
# UNDERSTANDING iter() AND next()
# ============================================================

# iter(dice)
#     ↓
# calls dice.__iter__()
#     ↓
# returns the iterator


# next(dice)
#     ↓
# calls dice.__next__()
#     ↓
# returns the next value


# ============================================================
# UNDERSTANDING StopIteration
# ============================================================

# raise normally raises an exception.
#
# StopIteration is a special exception used by iterators
# to tell Python that there are no more values.
#
# The for loop handles StopIteration automatically
# and stops the loop.


# ============================================================
# HOW THE DICE ITERATOR REMEMBERS ITS POSITION
# ============================================================

# dice = Dice(3)
#
# Initially:
# count = 0
# rolls = 3
#
# First next():
# count = 0 → 1 → returns a random number
#
# Second next():
# count = 1 → 2 → returns a random number
#
# Third next():
# count = 2 → 3 → returns a random number
#
# Fourth next():
# count = 3
# 3 < 3 is False
# → raises StopIteration
#
# count acts as the iterator's progress tracker.


# ============================================================
# QUICK REVISION
# ============================================================

# __iter__()
# → returns the iterator


# __next__()
# → returns the next item


# StopIteration
# → tells Python that the iterator is finished


# iter(object)
# → calls object.__iter__()


# next(object)
# → calls object.__next__()


# for loop
# → automatically uses iter() and next()
# → stops when StopIteration is raised