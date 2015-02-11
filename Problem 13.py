import sys
import math

filename = "test.csv"
with open(filename, 'r') as file:
	read_data = file.read()
read_data = read_data.split()

total = 0
for i in range(0,len(read_data)):
	total += int(read_data[i])

print(str(total)[:10])