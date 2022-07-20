'''
Script: Project Euler problem 22
James Philbrick, July 2022

names file saved in ../problem_files/p022_names.txt

working:
for each name in list: work out score and add to running sum.
'''

def read_names_into_list():
    # read names into list
    f = open('../problem_files/p022_names.txt', 'r')
    nameList = f.read().split(',')
    f.close()

    # remove quotation marks
    for i, name in enumerate(nameList):
        nameList[i] = name[1:-1]

    nameList.sort()
    return nameList


def calculate_score(pos, name):
    pos += 1 # humans count from 1
    score = 0

    # get letter pos in alphabet and add on to running total
    for letter in name:
        score += ord(letter) - 64

    score *= pos
    return score


def main():
    score = 0
    nameList = read_names_into_list()

    for pos, name in enumerate(nameList):
        score += calculate_score(pos, name)

    print(score)


if __name__ == '__main__':
    main()