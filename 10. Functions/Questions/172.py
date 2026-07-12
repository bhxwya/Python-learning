def str_palindrome (word : str):
    if word == word[::-1]:
        print("Your string is palindrome")
    else:
        print("Your string isn't palindrome")
    
str_palindrome("taat")