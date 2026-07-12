"""
Exception Handling

Purpose:
- Prevents the program from crashing when an error occurs.
- Lets the program continue running even after an error.

Syntax:

try:
    # Code that may cause an error

except:
    # Runs only if an error occurs in the try block

Execution Flow:
1. Python enters the try block.
2. If no error occurs:
      -> except block is skipped.
3. If an error occurs:
      -> Python immediately jumps to the except block.
      -> Remaining code inside try is NOT executed.
4. Program continues after the except block.
"""

try:
    lst = [4, 5, 5, 34, 2, 3, 6]

    print(lst[1])      # Works
    print(lst[65])     # Error (IndexError) (Without try-except, the program would crash here.)
    print(lst[2])      # Skipped
    print(lst[3])      # Skipped
    print(lst[4])      # Skipped

except:
    print("Some error occurred")

print("Done")
print("Bye")