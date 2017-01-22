#lab 1 ex 8
n = int(input())
sum = float(0)
m = float(1)
i = int(0)
while i <= n:
	sum = sum + m/(2*i + 1)
	m = -m
	i = i + 1
print(float(4 * sum))
