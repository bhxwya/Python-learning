# Append Mode ("a")
# - Opens the file for writing.
# - Existing content is NOT deleted.
# - New data is added at the end of the file.
# - File pointer starts at the end.
# - Creates the file if it doesn't exist.
# - write() returns the number of characters written.

with open("hello.txt", "a") as file:
    file.write("\nThis is a new line.")