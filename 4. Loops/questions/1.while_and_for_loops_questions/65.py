x = int(input("Enter your first number:"))
y = int(input("Enter your second number:"))


if x < y:
    for i in range (x, y + 1):
        print (i , end= " ")
        
else:
    for i in range (y, x + 1):
        print (i, end=" ")