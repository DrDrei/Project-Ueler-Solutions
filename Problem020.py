import sys
import math



def feb(year):
	if not (year % 4):
		return 29
	else:
		return 28

def months(month, year):
	if month == 4 or month == 6 or month == 9 or month == 11:
		return 30
	elif month == 2:
		return feb(year)
	else:
		return 31

count = 0
weekday = 0
for year in range(1901,2000+1):
	for month in range(1,13):
		for day in range(1,months(month,year)+1):
			weekday += 1
			if weekday == 8:
				weekday = 1
			if 1 == day and 1 == weekday:
				count += 1
				print(count)
			print(day,weekday,month,year)

print(count)