'''
Script: Project Euler problem 28
James Philbrick, July 2022

working:
I observed that the upper right diagonal for each 'layer' is simply n^2 
where n is the sidelength of that layer.
So to find the other 3 diagonals (ignoring the central '1'), we
simply subtract 1(n-1), 2(n-1), and 3(n-1). The sum of this set
is n^2 + n^2-n(n-1) + n^2-2n(n-1) + n^2-3n(n-1) which can be simplified
to

x = 4n^2 - 6n + 6

where x is the sum of the diagonals for a given 'layer', n.
n = {3, 5, 9...} and n !=1

calculate this for each layer and then add 1 to get the answer.
'''

def main():
    n = 1001 # define size of spiral
    runningTotal = 1

    # gonna work backwards, outside in
    if (n % 2 == 0) or (n < 3):
        print('Invalid n input')
    else:
        while n >= 3:
            runningTotal += (4*n**2 - 6*n + 6)
            n -= 2
        print(runningTotal)


if __name__ == '__main__':
    main()