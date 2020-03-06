def func():
    x = 2 ** 1000
    x = str(x)
    l1 = list(x)
    l2 = []
    for y in l1:
        y = int(y)
        l2.append(y)
    print(sum(l2))
func()
