from math import factorial

def f(x):
	l = []
	fact = 1
	while x > 1:
		fact *= x
		x -= 1
	l_1 = list(str(fact))
	for i in l_1:
		l.append(int(i))
	print(sum(l))
f(10)


def z(x):
	l = []
	fact = factorial(x)
	l_1 = list(str(fact))
	for i in l_1:
		l.append(int(i))
	print(sum(l))
z(10)
	
