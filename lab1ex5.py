import math
a = float(input())
b = float(input())
c = float(input())

d = b * b - 4 * a * c
if d == 0:
	print(int((-b / (2 * a) + 0)))
if d > 0:
	x = (-b + math.sqrt(d)) / (2 * a)
	x1 =  (- b - math.sqrt(d)) / (2 * a)
	print( x + " " + x1)
