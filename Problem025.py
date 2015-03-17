import sys 
import math

numbers = list(range(0,10))

def inc(numbers):
	#find largest
	index = len(numbers)-1
	maxi = max(numbers)
	while True:
		if numbers[index] > numbers[index-1]:
			pivot = index-1
			new = numbers[pivot:]
			new.sort()
			piv_val = numbers[pivot]
			piv_index = new.index(piv_val)
			new_piv_val = new[piv_index+1]
			for x in new:
				numbers.remove(x)
			numbers.append(new_piv_val)
			new.remove(new_piv_val)
			for x in new:
				numbers.append(x)
			break
		else:
			index -= 1			
	return numbers

count = 0
while count != 999999:
	inc(numbers)
	count += 1
print(numbers)