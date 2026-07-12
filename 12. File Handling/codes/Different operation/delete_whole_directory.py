import shutil
import os

# Deleting a directory and its contents
if os.path.exists("folder 2"):
    shutil.rmtree("folder 2")
    print("Directory and its contents deleted.")
else:
    print("Directory does not exist.")

# NOTES:
# import shutil        -> Imports the shutil module (Shell Utilities).
#                         It is used for advanced file and folder operations.
#
# import os            -> Imports the os module to work with files and folders.
#
# os.path.exists()     -> Checks whether the folder exists.
#
# shutil.rmtree()      -> Deletes a directory (folder) along with ALL
#                         the files and subfolders inside it.
#                         It can delete both empty and non-empty folders.
#
# if-else              -> Prevents an error by checking if the folder exists first.
#
# Difference:
# os.remove()    -> Deletes a file.
# os.rmdir()     -> Deletes an EMPTY folder only.
# shutil.rmtree()-> Deletes a folder and everything inside it.