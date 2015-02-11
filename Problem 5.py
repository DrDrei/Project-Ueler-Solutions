import sys
import math

test = []
for i in range(2,20+1):
	test.append(i)

count = 20
while True:
	filter = []
	for i in test:
		if (count % i) == 0:
			filter.append(1)
		else:
			break
	if len(filter) == len(test):
		break
	#test next number
	count += 20

print(count)