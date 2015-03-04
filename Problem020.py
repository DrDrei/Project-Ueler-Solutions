import sys 
import math

n = 100
product = 1
for i in range(1,n+1):
	product = product * i

product = str(product)
sum = 0
for i in product:
	sum += int(i)

print(sum)