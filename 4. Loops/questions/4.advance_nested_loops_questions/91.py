"""
@ @ @ @ 1
@ @ @ 2 1 2
@ @ 3 2 1 2 3
@ 4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
"""

x = 1
for i in range(5, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")

    for k in range(x, 0, -1):
        print(k, end=" ")
    
    for n in range(2, x + 1 ):
        print(n, end=" ")
    x += 1
    print()
    
    
    
    