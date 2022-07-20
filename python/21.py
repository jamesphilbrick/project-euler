
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def d(n):
	total = 0
	for i in range(1, n):
		if n % i == 0:
			total += i
	return total

def is_amicable(n):
	a = d(n)
	b = d(a)
	if b == n:
		return a, b
	else:
		return 0, 0

total = 0
for i in range(1, 10000):
	a, b = is_amicable(i)
	if a != b:
		print('amicable pair:', str(a), str(b))
		total += (a + b)

print(total/2) # for each pair that is found, it is found again in reverse order, so /2 at and to compensate

