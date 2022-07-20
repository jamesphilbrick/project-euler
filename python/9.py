# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

a = 0
b = 0
c = 0

# incriment a and b, such that they are natural numbers, and b > a. 
# calculate c. If a+b+c == 1000, then eureka

# if a < b < c, then the max value of a is bound by <1000/3, same goes for b.

# 332, 333, 335 are max val for a
# 1, 499, 500 are max val for b

for a in range(1, 332):
	for b in range(1, 499):
		# print(a, b)
		c = math.sqrt(a**2 + b**2)
		if c.is_integer() and a < b < c and (a + b + c == 1000):
			print('triplet:', str(a), str(b), str(c), '\ntotal:', str(a+b+c), '\nproduct:', str(a*b*c))
		else:
			continue