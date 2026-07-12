"""
Ask a string from user. Count the number of uppercase and
lowercase characters in that String.

"""

my_string = input("Enter a string = ")
uppercase_count = 0
lowercase_count = 0

for ch in my_string:
    # ascii = ord(ch)
    # if (ascii >= 65 and ascii <= 90):
    if (ch >= "A" and ch <= "Z"):

        uppercase_count += 1
    # elif (ascii >= 97 and ascii <= 122):
    elif (ch >= "a" and ch <= "z"):
        lowercase_count += 1

print(
    f"Uppercase character in your string is {uppercase_count} and lowercase character in your string is {lowercase_count}")
