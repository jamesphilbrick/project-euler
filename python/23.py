'''
Script: Project Euler problem 23
James Philbrick, July 2022

working:
note: proper divisors are divisors of a number which exclude that number itself
perfect number: sum(proper divisors) == number
if sum(proper divisors) < number, then 'deficient'
if sum(proper divisors) > number, then 'abundant'

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
i.e. for all integers <= 28123:
    if cannot be written as the sum of two abundant numbers, add to running total

so given any arbitrary positive integer, we need to be able to test if abundant or not.

a lot of headache and confusion could have been avoided if I had read the question properly: 
Find the sum of all the positive integers which cannot be written as the sum of TWO abundant numbers.
T W O abundant numbers! I was looking at exponentially expensive algorithms that dealt with combinations of 
summations in a set! 
'''

# return list of proper divisors for some int input
def get_proper_divisors(x):
    divisors = []
    for i in range(1, x):
        if x % i == 0:
            divisors.append(i)
        else: pass
    return divisors

def check_if_abundant(x):
    # get proper divisors
    divisors = get_proper_divisors(x)
    # sum divisors and compare
    if sum(divisors) > x:
        return True
    else: return False

# get list of all sums of two abundant numbers
def get_abundant_sums(abundantNumbers):
    abundantSums = []
    for i in abundantNumbers:
        for j in abundantNumbers:
            if (i + j) <= 28123:
                abundantSums.append((i + j))
    return abundantSums

def main():
    abundantNumbers = []
    for i in range(1, 28123 + 1):
        if check_if_abundant(i):
            abundantNumbers.append(i)
        else: pass
    print('generated abundant number list of len {}'.format(len(abundantNumbers)))

    abundantSums = get_abundant_sums(abundantNumbers)
    print('generated sum list of len {}'.format(len(abundantSums)))

    abundantSums = set(abundantSums)
    print('generated set of len {}'.format(len(abundantSums)))

    total = 0
    for i in range(1, 28123 + 1):
        if i not in abundantSums:
            total += i
        else: pass
    print('total = {}'.format(total))

if __name__ == '__main__':
    main()
