"""
@ @ @ @ *
@ @ @ * * *
@ @ * * * * *
@ * * * * * * *
* * * * * * * * *
"""
x = 1
for i in range(5, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
        
    for k in range(2*x-1):
        print("*", end=" ")
    x += 1
    print()
    
