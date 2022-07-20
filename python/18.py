'''
Script: Project Euler problem 18
James Philbrick, July 2022

My working:
on some index i along a row of numbers
index of next row: i or i+1

left: i -> i
right: i -> i+1

counting in binary. where left=0 and right=1
count from 00...0 to 11...1 where the length of the number == the number of rows - 1
so binary number (in denary) is 2^(r-1) where r is number of rows

for each number in binary: 
get the value at the current index (starting i=0)
depending on whether 1 or 0, adjust index accordingly
find value on next row at this current index and add on to total
rinse and repeat
'''

triangle = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65,  4, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

counter = 2**(15)

def get_binary_seq(x):
    binarySeq = str(bin(x)).split('b')[1]
    if len(binarySeq) < 15:
        binarySeq = binarySeq + ('0'*(15 - len(binarySeq)))
    else: pass
    return binarySeq

def get_sum_from_seq(binarySeq):
    sum = 75
    i = 0
    for n in range(1,15):
        if binarySeq[n] == '0':
            i += 0
            sum += triangle[n][i]
        elif binarySeq[n] == '1':
            i += 1
            sum += triangle[n][i]
    return sum

def main():
    greatestSum = 0

    for i in range(counter):
        binarySeq = get_binary_seq(i)
        sum = get_sum_from_seq(binarySeq)

        if sum > greatestSum:
            greatestSum = sum
        else: pass
    print(greatestSum)

if __name__ == '__main__':
    main()
