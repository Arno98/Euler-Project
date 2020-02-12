numbers = list(range(1001))
sum_numbers_n = []

for n in numbers:
	if n % 3 == 0 and n % 5 == 0:
		sum_numbers_n.append(n)

print(sum(sum_numbers_n))
