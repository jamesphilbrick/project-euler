
# if i % x == 0: --> if i is divisible by x

upper_bound = 1000
total = 0

for i in range(1, upper_bound):
	if (i % 3 == 0) or (i % 5 == 0):
		total += i
	else: pass

print(total)
