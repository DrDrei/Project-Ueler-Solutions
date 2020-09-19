import sys
import math

def value_return(n):
	if n % 2 == 0:
		return int(n/2)
	elif n % 2 == 1:
		return int(n*3+1)

sequence = [13]
count = 0
while sequence[-1] != 1:
	sequence.append(value_return(sequence[count]))
	count += 1
biggest = [0]
for i in range(500001,1000000,2):
	sequence = [i]
	count = 0
	while sequence[-1] != 1:
		sequence.append(value_return(sequence[count]))
		count += 1
	if (len(biggest) < len(sequence)):
		biggest = sequence

print(biggest)
print(len(biggest))