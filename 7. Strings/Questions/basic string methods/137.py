my_string = input("Enter a String = ")
alphabet_count = 0
spaces_count = 0
symbols_count = 0

for ch in my_string:
    ascii_value = ord(ch)
    if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):
        alphabet_count += 1
    elif ascii_value == 32:
        spaces_count += 1
    else:
        symbols_count += 1

print(f"The alphabet count in your string is {alphabet_count}")
print(f"The spaces count in your string is {spaces_count}")
print(f"The symbol count in your string is {symbols_count}")
