def spiral(a, b):
	numbers = list(range(1, a*b+1))
	diag_num = [1, 3, 5, 7, 9]
	
	last_num = diag_num[-1]
	quantity_num = 3
	step = 4
	
	while True:
		if diag_num[-1] != numbers[-1]:
			num_2 = numbers[last_num+quantity_num:(quantity_num*4+4)+last_num:step]
			for x in num_2:
				diag_num.append(x)
			quantity_num += 2
			step += 2
			last_num = diag_num[-1]
		else:
			break
	print(sum(diag_num))
	
spiral(1001, 1001)
