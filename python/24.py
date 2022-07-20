'''
Script: Project Euler problem 24
James Philbrick, July 2022

using itertools library out of laziness ("efficiency")
'''

import itertools

def get_permutation_list(digits):
    return(list(itertools.permutations(digits)))

def main():
    a = get_permutation_list([0,1,2,3,4,5,6,7,8,9])
    a.sort()
    result = a[1000000 - 1]
    print(''.join(str(e) for e in result))

if __name__ == '__main__':
    main()