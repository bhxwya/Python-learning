"""
@ @ @ @ *
@ @ @ * * *
@ @ * * * * *
@ * * * * * * *
* * * * * * * * *
@ * * * * * * *
@ @ * * * * *
@ @ @ * * *
@ @ @ @ *
"""
x = 1
for i in range(5 , 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(2*x-1):
        print("*", end=" ")
    x += 1
    print()


for l in range(4, 0, -1):
    for m in range(5, l, -1 ):
        print(" ", end=" ")
    for n in range(2*l-1):
        print("*", end= " ")
    print()
    
    
        



        