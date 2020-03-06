a = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8]
b = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0]
c = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65]
d = [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
e = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
f = [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
g = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
i = [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
k = [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
l = [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95]
m = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92]
n = [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57]
p = [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
q = [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40]
r = [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
s = [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
t = [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
v = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
w = [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
z = [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]

def mult(x):
	m = 1
	for y in x:
		m = m * y
	return m

def cut_list(x):
	row1 = x[:4]
	row2 = x[4:8]
	row3 = x[8:12]
	row4 = x[12:]

	col1 = [x[0], x[4], x[8], x[12]]
	col2 = [x[1], x[5], x[9], x[13]]
	col3 = [x[2], x[6], x[10], x[14]]
	col4 = [x[3], x[7], x[11], x[15]]

	diagonal1 = [x[0], x[5], x[10], x[15]]
	diagonal2 = [x[12], x[9], x[6], x[3]]

	global_list = [row1, row2, row3, row4, col1, col2, col3, col4, diagonal1, diagonal2]

	mult_values = []
	mult_mult_values = []
	max_mult_values = []

	for l in global_list:
		m = mult(l)
		mult_values.append(m)
	print(mult_values)
	print(max(mult_values))
	print("\n")

def count_list(z1, z2, z3, z4):
	mult_row1 = [z1[:4], z2[:4], z3[:4], z4[:4]]
	mult_row2 = [z1[4:8], z2[4:8], z3[4:8], z4[4:8]]
	mult_row3 = [z1[8:12], z2[8:12], z3[8:12], z4[8:12]]
	mult_row4 = [z1[12:16], z2[8:12], z3[8:12], z4[8:12]]
	mult_row5 = [z1[16:], z2[16:], z3[16:], z4[16:]]

	mult_block1 = []
	mult_block2 = []
	mult_block3 = []
	mult_block4 = []
	mult_block5 = []

	for block1 in mult_row1:
		for num in block1:
			mult_block1.append(num)
	for block2 in mult_row2:
		for num in block2:
			mult_block2.append(num)
	for block3 in mult_row3:
		for num in block3:
			mult_block3.append(num)
	for block4 in mult_row4:
		for num in block4:
			mult_block4.append(num)
	for block5 in mult_row5:
		for num in block5:
			mult_block5.append(num)
	
	global_mult_lists = [mult_block1, mult_block2, mult_block3, mult_block4, mult_block5]

	for l in global_mult_lists:
		cut_list(l)

count_list(a, b, c, d)
count_list(e, f, g, i)
count_list(k, l, m, n)
count_list(p, q, r, s)
count_list(t, v, w, z)
