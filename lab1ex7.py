# lab 1 ex 7

n = int(input())
'''
sum = int(1)
i = int(2)
for i in range (n+1):
	sum = sum + 1/(i**2)
print(sum)
'''

sum = float(0)
i = int(1)
while i < (n+1):
	sum = sum + 1/(i**2)
	i = i + 1
print(float(sum))
