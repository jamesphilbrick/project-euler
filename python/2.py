
upper_bound = 4000000
count = 0

def is_even(n):
	if n % 2 == 0:
		return True
	else:
		return False

# starting conditions
npast = 1
npres = 1

while npres < upper_bound:
	nfut = npast + npres
	npast = npres
	npres = nfut

	if is_even(npres):
		count += npres
		print(str(npres) + ' is even')
	else:
		pass

print('total: ' + str(count))