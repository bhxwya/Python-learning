"""        
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
  4 4 4 4
    3 3 3
      2 2
        1
"""
x = 5
for i in range(1, 6):
    for j in range(1, x):
        print(" ", end=" ")
    
    for k in range (0, i):
        print(i, end=" ")
    x -= 1
    print()

y = 1
for n in range (4, 0, -1):
    for m in range(0, y):
        print(" ", end=" ")
    
    for o in range (n):
        print(n, end=" ")
    
    y += 1
    print()
