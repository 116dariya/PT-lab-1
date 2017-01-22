# lab 1 ex 3
a = float(input())
b = float(input())
if a == 0 and b == 0:
	print('INF')
elif a == 0 and b != 0:
	print('NO')
else:
	x = -b/a
	x = int(x)
	if x == 0:
		print('NO')
	else:
		print(x)
