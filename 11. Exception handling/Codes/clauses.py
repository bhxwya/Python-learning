"""
Exception Handling Clauses

Clause:
- A clause is a part (block) of a statement that performs a specific task.

Exception handling uses these clauses:
1. try
2. except
3. else
4. finally (covered later)
"""

try:
    my_list = [2, 5, 6, 7, 88, 0]

    print(my_list[0])                  # Works
    # print(my_list[76])               # IndexError
    # print(my_list[0] / my_list[-1])  # ZeroDivisionError
    # my_list = my_list * "abc"        # TypeError

except IndexError:
    print("Invalid Index")

except ZeroDivisionError:
    print("You cannot divide by zero")

except:
    print("Some error occurred")

else:
    print("Everything worked fine")