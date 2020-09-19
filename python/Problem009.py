import sys
import math
import timeit

def pyth(a,b,c):
	if ((a**2)+(b**2)) == (c**2):
		return True
	else:
		return False
min = 1
max = 500
indexA = []
for i in range(min, max):
	indexA.append(i)
"""
#kinda slow ~ a minute
while indexA != []:
	a = indexA.pop(0)
	for b in range(min,max):
		for c in range(min,max):
			if (pyth(a,b,c) and ((a+b+c) == 1000)):
				print(a,b,c)
				print(a*b*c)
				indexA = []
"""

#much faster, gives two same values, but not a big issue.
for a in range(min,max):
	for b in range(min,max):
		c = math.sqrt(a**2+b**2)
		if (pyth(a,b,c) and ((a+b+c) == 1000)):
			print(a,b,int(c))
			print(int(a*b*c))
			break