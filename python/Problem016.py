import sys
import math

power = 1000

number = str(2 ** power)

total = 0
for i in number:
	total += int(i)

print(total)