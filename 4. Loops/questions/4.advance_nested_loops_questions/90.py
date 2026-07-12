"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
4 3 2 1
3 2 1
2 1
1
"""

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

for k in range(4, 0, -1):
    for l in range(k, 0, -1):
        print(l, end=" ")
    print()
