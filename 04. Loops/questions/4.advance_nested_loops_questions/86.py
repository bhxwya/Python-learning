"""
@ @ @ @ 1
@ @ @ 1 2
@ @ 1 2 3
@ 1 2 3 4
1 2 3 4 5
"""
x = 2
for i in range(5, 0, -1):
    for j in range(1, i):
        print("@", end=" ")
        
    for k in range(1, x):
        print(k, end=" ")
    x +=1
    print()