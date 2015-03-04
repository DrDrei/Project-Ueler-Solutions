import sys
import math

max_number = 10
index = []

for i in range(1,100+1):
	index.append(i)

# sum of squares
sosq = 0
sosum = 0
for j in index:
	sosq += j*j
	sosum += j
sosum = sosum*sosum
# square of sums
difference = sosum - sosq
print(difference)
