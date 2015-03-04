import sys 
import math

def memoize(bad_f):    
	import functools
	bad_f.memo = {}
	@functools.wraps(bad_f)
	def good_f(*args, **kwargs):
		my_key = repr(args) + repr(kwargs)
		if not my_key in bad_f.memo:
			bad_f.memo[my_key] = bad_f(*args, **kwargs)
		return bad_f.memo[my_key]
	return good_f

@memoize
def sums(number):
	factors = []
	for i in range(1,number):
		if not (number % i):
			factors.append(i)
	return factors

totals = 0
for i in range(1,10000):
	a = sum(sums(i))
	b = sum(sums(a))
	if b == i and a != b:
		totals += a

print(totals)