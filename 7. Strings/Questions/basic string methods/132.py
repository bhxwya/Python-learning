"""
Ask a string from user. Count how many alphabets are there in that
string.

"""

my_string = input("Enter a String = ")
count = 0

"""1st Method"""
for ch in my_string:
    ascii = ord(ch)
    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
        # if ('a' <= ch <='z') or ('A' <=ch <= 'Z'):
        count += 1

print(f"Count of the alphabet in your string is {count}")

"""2nd Method"""
# for ch in my_string:
#     if ch.isalpha():
#         count += 1

# print(f"Count of the alphabet in your string is {count}")
