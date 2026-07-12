my_string = input("Enter a String = ") #ansh123
count = 0

for ch in my_string:
    ascii_value = ord(ch)
    if ascii_value == 32:
        count += 1

print(count)
