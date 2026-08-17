# with automatically opens the file and closes it after the block finishes.
# No need to call file.close().

with open(r"D:\MY CODES\Python-learning\12. File Handling\codes\Read mode\hello.txt", "r") as file:

    # read() reads the ENTIRE file and returns it as one string.
    # x = file.read()

    # Since x is a string, iterating over it gives one character at a time.
    # for char in x:
    #     print(char)

    # A file object is iterable.
    # Looping directly over the file reads ONE LINE at a time.
    # Each iteration stores one line in the variable 'i'.
    # for i in file:
    #     print(i)

    # Printing the file object itself DOES NOT print the file's contents.
    # It only shows information about the file object, such as:
    # <_io.TextIOWrapper name='hello.txt' mode='r' encoding='utf-8'>
    print(file)