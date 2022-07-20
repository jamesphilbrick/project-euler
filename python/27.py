'''
Script: Project Euler problem 26
James Philbrick, July 2022

a: -999  -> 999
b: -1000 -> 1000
'''

def is_prime(n):
    # implementation of complexity O(sqrt(N))
    if n <= 1:
        return False
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def get_len_consec_primes(a, b):
    lenConsecPrimes = 0
    n = 0
    while True:
        if is_prime(n**2 + a*n + b):
            lenConsecPrimes += 1
            n += 1
        else:
            break
    return lenConsecPrimes

def main():
    maxLenConsecPrimes = 0
    coeffProduct = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            lenConsecutivePrimes = get_len_consec_primes(a, b)
            if lenConsecutivePrimes > maxLenConsecPrimes:
                maxLenConsecPrimes = lenConsecutivePrimes
                coeffProduct = a*b
            else:
                pass
    print(coeffProduct)

if __name__ == '__main__':
    main()