# def table(num : int) -> None: #(it's just a hint)
def table(num) -> None:
    # num = int(num)
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

table("h")