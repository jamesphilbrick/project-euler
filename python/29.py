'''
Script: Project Euler problem 29
James Philbrick, July 2022

two 2d grids of size (a-1)(b-1): g1 and g2
for each item in g1:
    compare to each item in g2 and if equal, add to duplicateCount

ans = size(g) - duplicateCount/2
'''
from math import log

def main():
    a, b = 100, 100
    duplicateCount = 0

    for g1a in range(2, a+1):
        for g1b in range(2, b+1):
            # for each item in g1
            for g2a in range(2, a+1):
                for g2b in range(2, b+1):
                    # for each item in g2

                    if (log(g1a)/g2b == log(g2a)/g1b) and not (g1a == g2a):
                        duplicateCount += 1
                        # print('{}^{} == {}^{}'.format(g1a, g1b, g2a, g2b))
                    else:
                        pass
    seqLen = (a-1)*(b-1)
    print(seqLen)
    print(duplicateCount)
    print(seqLen - (duplicateCount/2)) 

# def check_duplicates(a,b, size):
#     n = 2
#     duplicateCount = 0
#     while (a**n <= size):
#         # print('a = {} and b = {}'.format(a, b))
#         duplicateCount += 1
#         n += 1
#     return duplicateCount

# def main():
#     size = 100
#     duplicateCount = 0
#     for a in range(2, size+1):
#         for b in range(2, size+1):
#             duplicateCount += check_duplicates(a,b, size)
#     print(duplicateCount)
#     print((size-1)*(size-1) - duplicateCount)

if __name__ == '__main__':
    main()