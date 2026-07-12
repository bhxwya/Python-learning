def freq_string (word : str):
    my_dict = {}
    for ch in word:
        if ch not in my_dict:
            my_dict[ch] = 1
        else:
            my_dict[ch] += 1
    
    for k,v in my_dict.items():
        print(f"{k} occurs {v} times")
        
freq_string("hyyyyyyl90")
            
