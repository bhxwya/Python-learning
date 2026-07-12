"""
Write a Python program that takes a username as input and performs the following tasks:
Remove any leading and trailing spaces.
Check if the username starts with "@".
If it doesn't, add "@" at the beginning.
Replace every space inside the username with an underscore (_).
Count how many underscores (_) are present.
Check if the username ends with "_admin".
Find the position of the first underscore.
If there is no underscore, print "No underscore found".
Find the position of the letter 'a' using:
find()
index()
Observe what happens if 'a' doesn't exist. 

"""

username = input("Enter a username: ")
username = username.strip()

if not username.startswith("@"):
    username = "@" + username

    # my_list = username.split()
    # my_list.insert(0, "@")
    # username = " ".join(my_list)
username = username.replace(" ", "_")

print(f"Clean Username: {username}")

print(f"Starts with @: {username.startswith('@')}")

print(f"Ends with _admin: {username.endswith('_admin')}")

print(f"Underscore Count: {username.count('_')}")

if username.find("_") == -1:
    print("No underscore found")
else:
    print(f"First Underscore Index: {username.find('_')}")

print(f"'a' found using find(): {username.find('a')}")

if username.find("a") != -1:
    print(f"'a' found using index() {username.index('a')}")