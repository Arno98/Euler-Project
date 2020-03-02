def prime(x):
	for y in range(2, x):
		if x % y == 0:
			break
	else:
		print(x)
		
def dividings_of_number(y):
	dividings = []
	for n in range(1, y):
		if y % n == 0:
			dividings.append(n)
	for d in dividings:
		a = prime(d)
		p.append(a)
dividings_of_number(600851475143)
