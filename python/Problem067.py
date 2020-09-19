import sys
import math

#bottom up with sub-problems
#impliment a triangle calculation
def calc_max(file):
	storage = []
	new = []
	with open(file, 'r') as infile:
		for line in infile:
			storage.append(list(map(int,line.strip().split(" "))))
			new.append(list(map(int,line.strip().split(" "))))

	for i in range(len(new)-1):
		for j in range(len(new[i+1])-1):
			a,b = tri(new[i][j],storage[i+1][j],storage[i+1][j+1])
			if a > new[i+1][j]:
				new[i+1][j] = a
			new[i+1][j+1] = b
	return max(new[i+1])

def tri(top, left, right):
	return top+left,top+right
	

file = "Problem067.txt"
print(calc_max(file))
