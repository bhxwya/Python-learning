# import
# Used to access pre-written code from Python modules.

# os Module
# - Stands for Operating System.
# - Helps Python interact with files and folders.
# - Provides functions like rename(), remove(), mkdir(), etc.

# os.path.exists(path)
# - Checks whether a file or folder exists.
# - Returns True if it exists.
# - Returns False otherwise.

# os.rename(old_name, new_name)
# - Renames a file or folder.
# - Takes two arguments:
#   1. Old name/path
#   2. New name/path

# The dot (.) is used to access functions or objects
# that belong to a module or object.

import os

if os.path.exists("hello.txt"):
    os.rename("hello.txt", "new_hello.txt")
    print("file renamed")
else:
    print("such a file doesn't exist")