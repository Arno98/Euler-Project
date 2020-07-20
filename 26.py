x = 2
l = {}
v = []
while x != 1001:
	action = 1 / x
	action = str(action)
	l[action] = len(action) - 2
	x += 1

for x in l:
	v.append(l[x])

for x in l:
	if l[x] == max(v):
		print(x)
