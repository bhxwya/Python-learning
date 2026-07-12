import os
if os.path.exists("new_hello.txt"):
    os.remove("new_hello.txt")
    print("File deleted")
else:
    print("such a file doesn't exists")