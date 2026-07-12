a = 12
b = 34
x = 23
y = 23
z = 13
n = 34

print(a > b)
print(a < b)
print(x >= y)
print(z <= n)
print(a != b)
print(x != y)

""" Voting System """

age = int(input("Enter your age :"))

if age > 120:
    print("Invalid")

elif age >= 18:
    print("You can vote")

else:
    print("Not eligble to vote")
