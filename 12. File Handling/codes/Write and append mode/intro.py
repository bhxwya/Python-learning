# "w" (Write Mode)
# - Opens the file for writing.
# - If the file already exists, ALL previous content is deleted (overwritten).
# - If the file does not exist, Python creates a new file.
# - After opening, the file pointer starts at the beginning (position 0).

with open("hello.txt", "w") as f:
    
    # f.write("kya hi bhay koi kaam nhi hai kya")
    
    f.write("Hello jaggery\n")
    f.write("How are you my puttar\n")
    f.write("sojayo")