numbers = []
a = 2
b = 2

while a <= 100:
	x = a ** b
	b += 1
	if x not in numbers:
		numbers.append(x)
	if b > 100:
		a += 1
		b = 2
print(len(numbers))

