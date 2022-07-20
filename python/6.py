limit = 100
def sum_squares():
	total = 0
	for i in range(1, limit+1):
		total += i**2
	return total

def square_sums():
	total = 0
	for i in range(1, limit+1):
		total += i
	return total**2

print(square_sums() - sum_squares())