def t_fibonacci():
	fibo_n = [1, 1]
	while True:
		plus = fibo_n[-1] + fibo_n[-2]
		str_plus = str(plus)
		if len(str_plus) != 1000:
			fibo_n.append(plus)
			continue
		else:
			print(str_plus)
			break
				
t_fibonacci()
	
