import sys 
import math

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
filename = "Problem022.txt"
alphDict = {}
count = 1
for x in alph: 							# map the alphabet
	alphDict[x] = count
	count += 1
data = []
newdata = []
#--------------------------------------------------------
with open(filename, 'r') as filetxt:	# read from file
	for line in filetxt:
		data = line.split(",")			# split the line into "NAME-X"
	for x in data:
		newdata.append(x[1:-1]) 		# format data
		newdata.sort()
#--------------------------------------------------------
count = 1
names = {}
for x in newdata:						# map the names to corresponding numbers	
	names[x] = count
	count += 1

#--------------------------------------------------------
mappedData = {}
total = 0
for x in newdata:
	sum = 0
	for i in x:
		sum += alphDict[i]
	total += sum * names[x]
print(totals)


#with open(filename, 'r') as filetxt:
#	for line in filetxt:
#		print("hi")
