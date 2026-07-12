my_string = input("Enter a String = ")
result = ""

for ch in my_string:
    ascii_value = ord(ch)
    if ascii_value >= 97 and ascii_value <= 122:
        ascii_value = ascii_value-32
        ch = chr(ascii_value)
        result = result + ch

    elif ascii_value >= 65 and ascii_value <= 90:
        ascii_value = ascii_value+32
        ch = chr(ascii_value)
        result = result + ch

    else:
        result = result + ch
print(result)

# print(my_string.swapcase())
