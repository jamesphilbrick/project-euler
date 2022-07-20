
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?


from numba import jit

prime_limit = 10001
prime_count = 0
n = 0

@jit(nopython=True)
def check_if_prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

while prime_count != (prime_limit+1):
	n += 1
	if check_if_prime(n):
		prime_count += 1
	else:
		continue

print(str(n) + ' is prime (number ' + str(prime_limit) + ')')