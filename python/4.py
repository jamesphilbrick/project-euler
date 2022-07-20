number_digits = 3

starting_value = 10**(number_digits-1)
maximum = 10**(number_digits)

a = starting_value
b = starting_value

largest_palindrome = 0

def is_palindrome(num):
	if str(num) == (str(num)[::-1]):
		return True
	else:
		return False



while a < maximum:
	while b < maximum:
		c = a*b
		if is_palindrome(c):
			print(str(c) + ' is a palindrome')
			if c > largest_palindrome:
				largest_palindrome = c
				a_palindrome = a
				b_palindrome = b
			else:
				pass
		else:
			pass
		b += 1
	b = starting_value
	a += 1

print('largest palindrome:', largest_palindrome, '('+str(a_palindrome), 'x', str(b_palindrome)+')')