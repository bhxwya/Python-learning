def largest_num(x: int, y: int, z: int):
    if x >= y and x >= z:
        print(f"{x} is the largest number")
    elif y >= x and y >= z:
        print(f"{y} is the largest number")
    else:
        print(f"{z} is the largest number")


largest_num(87, 34, 5)
