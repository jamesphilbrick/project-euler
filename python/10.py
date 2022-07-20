# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
from numba import jit

upper_bound = 2000000

@jit(nopython=True)
def check_if_prime(n):
	for i in range(2, n//2):
		if n % i == 0:
			return False
	return True

total = 0

n = 1
while n+2 < upper_bound:
	n += 2
	if check_if_prime(n):
		# print('prime found: '+str(n))
		total += n
	else:
		continue

print('total(including 2): '+ str(total+2))