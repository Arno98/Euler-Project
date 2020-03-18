def sum_primes_numbers():
    primes = []
    range_num = range(2, 1000001)
    for x in range_num:
        flag = True
        for y in range(2, x):
            if x % y == 0:
                flag = False
        if flag:
            primes.append(x)
    print(primes)
    print(sum(primes))
sum_primes_numbers()
