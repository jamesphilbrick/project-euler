from numba import jit

n = 0
numberFound = False
limit = 20 #const

@jit(nopython=True)
def check_if_divisible(n):
	for i in range(1, limit+1):
		if n % i != 0:
			return False
		else:
			continue
	return True

while numberFound == False:
	n += 2 #number must be even if able to divide by all numbers 1 to 20
	if check_if_divisible(n):
		print(str(n) + ' found')
		numberFound = True
	else:
		pass