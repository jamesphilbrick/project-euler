# what is the largest prime factor of the number below:

n = 600851475143

i = 2

while i * i < n:
    while n%i == 0:
        n = n / i
    i = i + 1

print (n)


# if confused, look at: https://www.mathsisfun.com/prime-factorization.html