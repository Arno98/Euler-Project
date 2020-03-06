list_range = list(range(1, 101))
sum_sqrt_l = []
sqrt_sum = sum(list_range) ** 2

for x in list_range:
    sum_sqrt_l.append(x**2)
sum_sqrt = sum(sum_sqrt_l)

print(sqrt_sum)
print(sum_sqrt)

print(sqrt_sum - sum_sqrt)
