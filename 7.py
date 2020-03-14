def len_prime_number():
    primes = [2]
    next_prime = 3
    while len(primes) != 10:
        flag = True
        for x in range(2, next_prime):
            if next_prime % x == 0:
                next_prime += 1
                flag = False
        if flag:
            primes.append(next_prime)
            next_prime += 1
    print(primes)
len_prime_number()
