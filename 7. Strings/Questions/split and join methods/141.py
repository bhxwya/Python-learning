
my_string = "helloWorldHowAreYou"
result = ""


for ch in my_string:
    ascii_value = ord(ch)
    if 65 <= ascii_value <= 90:
        result += "_" + chr(ascii_value + 32)
    else:
        result += ch

print(result)
