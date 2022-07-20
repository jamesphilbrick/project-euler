import math
import decimal
decimal.getcontext().prec = 1000

t1 = decimal.Decimal(1/math.sqrt(5))
t2 = decimal.Decimal((1+math.sqrt(5))/2)
t3 = decimal.Decimal((1-math.sqrt(5))/2)

target_digits = 1000

def getFn(n):
	return round(t1*((t2**n)-(t3**n)))

def countFibDigits(n):
	return len(str(getFn(n)))

n = 0
while True:
	n += 1
	if countFibDigits(n) == target_digits:
		print(getFn(n), 'is the first term to have', target_digits, 'digits, index =', n)
		break
	else:
		pass

# fib_old = 1
# fib = 1
# while True:
# 	fib = fib + fib_old