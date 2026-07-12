"""
Ask a string from user. Convert all the alphabets to uppercase.

"""

my_string = input("Enter a String = ") #ansh
# print(my_string.upper()) #ANSH
result = ""

for ch in my_string: #'a'
    ascii = ord(ch)   # 97
    if (ascii >= 97 and ascii <= 122):
        ascii = ascii - 32 #65
        ch = chr(ascii) #A
        result = result + ch
    else:
        result = result + ch

print(result)
    