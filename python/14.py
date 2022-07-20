
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

from numba import jit

n_largest_chain = 0
largest_chain = 0
max_num = 1000000


@jit(nopython=True)
def count_colatz_terms(n):
	number_terms = 0
	while n > 1:
		number_terms += 1
		if n%2 == 0: # if n is even
			n = n/2
		else:
			n = 3*n + 1
	return number_terms + 1 # to include the final 1 term that doesn't iterate the while loop

for i in range(1, max_num):
	n = count_colatz_terms(i)
	if n > largest_chain:
		largest_chain = n
		n_largest_chain = i 
	else:
		pass

print(str(largest_chain), 'is the largest chain with starting value', str(n_largest_chain)) 