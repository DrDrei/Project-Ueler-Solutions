import sys
import math

def prime(x):
	for i in range(2,int(math.sqrt(x)+1)):
		if (x % i) == 0:
			return False
	return True

count = 3
sum = 2
while count < 2000000:
	if prime(count) == True:
		sum += count
	count += 2
print(sum)