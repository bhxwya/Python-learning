x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

if x < y:
    while x <= y:
        print (x,  end= " ")
        x += 1
        
elif y < x:
    while y <= x:
        print (y,  end= " ")
        y += 1

        