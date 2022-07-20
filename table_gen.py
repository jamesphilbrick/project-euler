'''
python 3.10.1
script: generate github markdown file; table w/ list of problems
...each row has a link to the problem on the site as well as information 
...as to which language(s) were used to solve it.

James Philbrick, July 2022

This code is not very readable.
'''

import os

numberProblems = 50
heading = 'Problem | Language | Completed?'
langs = ['python']
exts = ['.py']

# create github markdown formatted string for a specific problem
def format_line(problemNumber, langs):
    if len(langs) != 0:
        problemCompleted = ':heavy_check_mark:'
    else: problemCompleted = ':x:'

    langString = ''
    for l in langs:
        langString = langString + ' ' + l
    
    line = '[' + str(problemNumber) + ']' + '(' + 'https://projecteuler.net/problem=' + str(problemNumber) +')' + ' | ' + langString + ' | ' + str(problemCompleted)
    
    return line

def write_line_to_file(line):
    f = open('table.md', 'a')
    f.write('\n')
    f.write(line)
    f.close()

def main():
    # write initial header
    write_line_to_file('Problem | Language | Completed?')
    write_line_to_file('-- | -- | --')

    for i in range(1, numberProblems+1):
        tempLangs = []
        for j in range(len(langs)):
            if (str(i)+exts[j]) in os.listdir(os.getcwd() + '/' + langs[j]):
                tempLangs.append(langs[j])
            else: pass
        line = format_line(i, tempLangs)
        write_line_to_file(line)

# remove old file so that new file can be created and written
def remove_old_file():
    try:
        os.remove('table.md')
    except: pass

# main
if __name__ == '__main__':
    remove_old_file()
    main()