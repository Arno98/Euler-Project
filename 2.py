def fibonacci():
	list_of_numbers = [1, 2]
	while len(list_of_numbers) != 100:
		next_n = list_of_numbers[-1] + list_of_numbers[-2]
		list_of_numbers.append(next_n)
	print(list_of_numbers)

fibonacci()
