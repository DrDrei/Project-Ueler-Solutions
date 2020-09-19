import sys
import math



def prime(x):
	for i in range(2,int(math.sqrt(x)+1)):
		if (x % i) == 0:
			return False
	return True

primes = [2]
number = 1000000
for v in range(3, number+1, 2):
	if prime(v) == True:
		primes.append(v)
print(primes)
print(primes[-1]*primes[-1])

test = 600851475143
for i in reversed(primes):
	if (test % i) == 0:
		print(i)