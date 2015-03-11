import sys 
import math


def factors(number):
	factor_list = []
	for i in range(1,round(number/2+1)):
		if not (number % i):
			factor_list.append(i)
	return factor_list

print("finding abuntant numbers")
total = []
for i in range(1, 28123):
	number = factors(i)
	if sum(number) > i:
		total.append(i)

print("creating clean array")
non_abund = set()
for x in range(1,28123):
	non_abund.add(x)

print("building sum of abundances")
sum_of_abund = []
buffer = total
for x in total:
	for y in buffer:
		if x+y < 28123:
			sum_of_abund.append(x+y)
	buffer.pop()

print("cleaning abundancies")
found = set()
new = []
for item in sum_of_abund:
	if item not in found:
		new.append(item)
		found.add(item)

print("removing sums of abundant numbers from clean array")
for x in new:
	non_abund.remove(x)
print(sum(non_abund))