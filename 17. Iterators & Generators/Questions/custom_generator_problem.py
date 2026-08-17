def even_numbers(n):
    num = 1
    while num <= n:
        if num % 2 == 0:
            yield num
        num += 1



for number in even_numbers(10000000):
    print(number)
