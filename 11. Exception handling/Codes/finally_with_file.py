file = None

try:
    file = open(r"D:\MY CODES\Python-learning\11. Exception handling\Codes\data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    if file is not None:
        file.close()
        print("File closed.")
