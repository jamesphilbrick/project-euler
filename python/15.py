
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

# n * n grid.

import math

grid_size = 20

def n_combinations(n):
	a = (2*n)-1
	b = n
	n = math.factorial(a)/(math.factorial(n)*math.factorial(a-n))
	return n

print('total routes:', str(n_combinations(grid_size)*2))
