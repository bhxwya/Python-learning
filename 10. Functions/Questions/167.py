def odd_even (num : int):
    if not isinstance(num, int):
        raise TypeError ("num must be an integar")
    
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
            
            
odd_even(11)