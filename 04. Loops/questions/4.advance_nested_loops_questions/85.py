"""
@ @ @ @ *
@ @ @ * *
@ @ * * *
@ * * * *
* * * * *
"""

x = 5
for i in range(1, 6):
    for j in range(1, x):
        print(" ", end=" ")   
    x -= 1
    
    for k in range(i):
        print("*", end=" ")
    print()
    