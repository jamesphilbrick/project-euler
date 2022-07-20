# 1 - 20 = unique

# 21 - 99 = simply pair tens and unit
# 100 - 999 = simply do same but with hundreds place with "and"

# 1000 = unique


# if no tens: number
# if between 10 and 20:

# break down into 100s, 10s, 1s:
	
# 	122 becomes 1*100, 2*10, 2*1
# 	if number not between 1 and 19?
# 		*1* hundred *and* twenty two
# 	elif number < 10: # 1-9
# 		print number
# 	elif number == 10: # 10
# 		print(ten)
# 	elif number > 20: # 11-19
# 		print from dict

digits = ['ten', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['ten', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

final_string = ''

def get_string_from_number(n):
	done = False
	while not done:
		if len(n) == 3:
			value = int(n[0])
			string = (digits[value] + 'hundred')
			if n[1] == '0' and n[2] == '0':
				done = True
			else:
				string = string + 'and'
				if n[1] == '0':
					string = string + digits[int(n[2])]
					done = True
				elif n[1] == '1':
					string = string + teens[int(n[2])]
					done = True
				else:
					if n[2] == '0':
						string = string + tens[int(n[1])]
					else:
						string = string + tens[int(n[1])] + digits[int(n[2])]
			done = True
		elif len(n) == 2:
			string = ''
			if n[1] == '0':
				string = string + tens[int(n[0])]
				done = True
			elif n[0] == '1':
				string = string + teens[int(n[1])]
				done = True
			else:
				string = string + tens[int(n[0])] + digits[int(n[1])]
				done = True
		elif len(n) == 1:
			string = digits[int(n)]
			done = True
	return string

number = 999
total = 0
for i in range(1, number + 1):
	total += len(get_string_from_number(str(i)))
	print(get_string_from_number(str(i)))
	# print(len(final_string) + 11)  # 'one thousand'

print(total + 11)
