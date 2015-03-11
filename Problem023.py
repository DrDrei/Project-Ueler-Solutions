import sys 
import math


def factors(number):
	factor_list = []
	for i in range(1,round(number/2+1)):
		if not (number % i):
			factor_list.append(i)
	return factor_list

print("finding factors")
total = []
for i in range(1, 23123):
	number = factors(i)
	if sum(number) > i:
		total.append(i)

print("finding sums of abundant numbers")
sum_of_abund = []
buffer = total
for x in total:
	for y in buffer:
		if x+y < 23123:
			sum_of_abund.append(x+y)
	buffer.pop()

print("removing duplicates")
new = []
for i in sum_of_abund:
	if i not in new:
		new.append(i)
print("creating clean array")
non_abund = []
for x in range(1,23123):
	non_abund.append(x)

print("removing sums of abundant numbers from clean array")
for x in new:
	try:
		non_abund.remove(x)
	except:
		pass


print(sum(non_abund))