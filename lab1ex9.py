# lab 1 ex 9
'''
x = None
array = []
while x != 0:
	x = int(input())
	array.append(x)
i = int(0)
maxi = int(array.index(x))
while i < array.count(x):
	if maxi < array.[i]
'''
array= []
while True:
	i = int(input())
	if i==0:
		break
	else:
		array.append(i)
max = array[0]

m=1
while m<len(array):
	if max<array[m]:
		max=array[m]
	m += 1

print(max)