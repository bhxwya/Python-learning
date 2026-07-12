
#(start,stop,step)

for i in range(1, 11):
    print(i, end=" ")
print()

for i in range(1, 12, 1):  # called step (1 is default)
    print(i, end=" ")
print()

for i in range(1, 11, 3):
    print(i, end=" ")
print()
    
for i in range(11, 0, -1): # 1 is default not -1 so it will not show any output, you gotta put -1 there
    print(i, end=" ")
print()