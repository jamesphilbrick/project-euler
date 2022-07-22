'''
Script: Project Euler problem 30
James Philbrick, July 2022

I've assumed that all answers are below 1000000 which seems to give 
the correct answer; I'm not sure how you would find this upper limit though...
'''
def main():
    n = 5
    runningTotal = 0
    for num in range(2, 1000000 + 1):
        digitList = [int(i) for i in str(num)]
        digitListRaised = [int(i**n) for i in digitList]
        if sum(digitListRaised) == num:
            print(num)
            runningTotal += num
        else:
            pass
    print(runningTotal)

if __name__ == '__main__':
    main()