def collatz():
    num_range = range(2, 1000000)
    col_dict = {}
    len_values = []
    for x in num_range:
        col = [x]
        while col[-1] != 1:
            if col[-1] % 2 == 0:
                d = col[-1] / 2
                col.append(d)
            else:
                d = (col[-1] * 3) + 1
                col.append(d)
        col_dict[x] = col
	    
    for x in col_dict.values():
        len_values.append(len(x))
        
    for k, v in col_dict.items():
        m = max(len_values)
        if len(v) == m:
            print(k, v)

collatz()
		
