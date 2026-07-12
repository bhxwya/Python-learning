"""
Multiple Exception Handling

Purpose:
- Handle different exceptions with different messages.
- Python checks each except block from top to bottom.
- The first matching except block is executed.
- If no specific exception matches, the generic except block runs.
"""

try:
    my_list = [2, 5, 6, 7, 88, 0]

    # print(my_list[76])              # IndexError
    # print(my_list[0] / my_list[-1]) # ZeroDivisionError
    my_list = my_list * "abc"         # TypeError

except IndexError:
    print("Invalid Index")

except ZeroDivisionError:
    print("You cannot divide by zero")

except:
    print("Some error occurred")