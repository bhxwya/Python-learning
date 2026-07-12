import os

# Deleting an empty directory
if os.path.exists("folder 1"):
    os.rmdir("folder 1")   # Remove directory
    print("Directory deleted.")
else:
    print("Directory does not exist.")

# NOTES:
# import os            -> Imports the os module to work with files and folders.
# os.path.exists()     -> Checks if the folder exists.
# os.rmdir()           -> Deletes an EMPTY directory (folder).
#                        If the folder contains any files or subfolders,
#                        it raises an OSError.
# if-else              -> Prevents an error by checking if the folder exists first.
#
# Difference:
# os.remove() -> Deletes a file.
# os.rmdir()  -> Deletes an empty folder (directory).