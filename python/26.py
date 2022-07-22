'''
Script: Project Euler problem 26
James Philbrick, July 2022

for each number 2-999:
    find the recurring cycle
    if longest, update index var (answer)

so how find the longest cycle?

this is a useful resource:
https://math.stackexchange.com/questions/377683/length-of-period-of-decimal-expansion-of-a-fraction?rq=1
https://en.wikipedia.org/wiki/Modular_arithmetic
to check that Euler's totient function works: https://oeis.org/A000010

'''
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def euler_totient(n):
    # return phi(n)
    ans = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            ans += 1
    return ans

def n_satisfaction_set(n):
    # find all factors of phi(n)
    s = set([])
    eulTot = euler_totient(n)
    for i in range(1, eulTot+1):
        if eulTot % i == 0:
            s.add(i)
        else:
            pass
    return sorted(s)

def find_ans_from_set(s, d):
    # find smallest n in set s which satisfies: 10**n % d == 1
    # since the set is already in ascending order, first number to
    # pass the test can be returned as the answer

    # this function can be made more efficient by implimenting binary 
    # exponentiation with binary and whatnot but since we're not playing with super large numbers,
    # I don't think it's too much of a problem at all
    for n in s:
        if (10**n) % d == 1:
            return n
        else: 
            pass
    return 0

def main():
    # so this doesn't seem to catch all cases: eg. 1/14 is 07142857142857142
    # but this isn't caught as a 6 digit recurring decimal according to the PE definition.
    # I'm just gonna sweep this under the rug knowning that it does seem to be accounted 
    # for in the set, even if it isn't found to be the answer
    longestRepeat = 0
    for d in range(2, 1000):
        s = n_satisfaction_set(d)
        currentRepeat = find_ans_from_set(s, d)
        if currentRepeat > longestRepeat:
            longestRepeat = currentRepeat
            print(d, currentRepeat)
        else:
            pass

if __name__ == '__main__':
    main()