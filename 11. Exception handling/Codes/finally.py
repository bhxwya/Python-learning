"""
finally Clause

Purpose:
- Executes whether an exception occurs or not.
- Always runs before the program leaves the try-except statement.
- Commonly used for cleanup tasks (closing files, database connections, etc.).
"""

try:
    my_list = [2, 5, 6, 7, 88, 0]

    print(my_list[0])
    print(my_list[0] / my_list[-1])    # ZeroDivisionError
    # my_list = my_list * "abc"        # TypeError

except IndexError:
    print("Invalid Index")

except ZeroDivisionError:
    print("You cannot divide by zero")

except:
    print("Some error occurred")

finally:
    print("This is a finally clause")