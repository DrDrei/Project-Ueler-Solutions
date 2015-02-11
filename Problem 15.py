import sys
import math
grid = 20
test = [[1] * (grid+1) for i in range(grid+1)]
for i in range(1,grid+1):
	for j in range(1,grid+1):
		try:
			test[i][j] = test[i-1][j]+test[i][j-1]
		except:
			pass
print(test[i][j])