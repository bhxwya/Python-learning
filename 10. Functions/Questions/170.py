def lst_avg(lst):
    total = 0
    for i in lst:
        total = total + i 
    
    avg = total / len(lst)
    print(f"Your average of the list is {avg:.2f}")


lst_avg([98, 3, 4, 34, 21, 34])
