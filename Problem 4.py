import sys
import math

first = 999
second = 999
stored = []
for i in range(int(first/2), first):
	for j in range(int(second/2), second):
		test = i * j
		stored.append(test)

stored = sorted(stored)
count = -1

while True:
	test = str(stored[count])
	if test == test[::-1]:
		print(test)
		break
	count -= 1