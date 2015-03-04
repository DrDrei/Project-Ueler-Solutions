import sys
import math

divisors = 0
count = 1
tri = 0
factors = []

# kinda slow.... ~2min?
while divisors < 500:
	factors = []
	tri = tri + count
	count2 = 1
	for i in range(1, int(tri/2+1)):
		if i in factors:
			break
		elif tri % i == 0 :
			factors.append(i)
			factors.append(int(tri/i))
			if tri/i == i:
				factors.remove(i)
	divisors = len(factors)
	count += 1

print(tri)