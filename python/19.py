'''
Script: Project Euler problem 19
James Philbrick, July 2022

Different methods for calculating a day based on a date: 
* Zeller's rule
* Key-Value Method
(according to https://beginnersbook.com/2013/04/calculating-day-given-date/)
Alternatively, there are libraries that allow this to be done in a single line, but
I won't learn anything by doing that and so I think I should impliment one of the 
methods above. I think Zeller's rule is a little simpler and so I'll take that approach.

Note: since I'm British, I'm using the DD/MM/YY format.
'''

def generate_dates():
    # list of strings of all first-of-the-month dates (01/01/1901 -> 01/12/2000)
    # list (non-static) will be of length 99*12 = 1188 which isn't too great for 
    # performance I don't think but if needed, could fetch the date each iteration 
    # instead of pre-generating a list at run time.
    dates = [] 

    for year in range(1901, 2000 + 1):
        for month in range(1, 12 + 1):
            dateString = '1.{}.{}'.format(month, year)
            dates.append(dateString)
    return dates

# apply Zeller's formula and return date number (Sunday == 0)
def get_day_from_date(date):

    monthMap = {1: 11, 2:12, 3:1, 4:2, 5:3, 6:4, 7:5, 8:6, 9:7, 10:8, 11:9, 12:10}

    k = 1                               # day of month
    m = int( date.split('.')[1]       ) # month number
    C = int( (date.split('.')[2])[:2] ) # first 2 digits of year
    D = int( (date.split('.')[2])[2:] ) # last 2 digits of year
    m = monthMap[m]

    F = k + int((13 * m-1)/5) + D + int(D/4) + int(C/4) - 2*C
    
    return F % 7


def main():
    numberSundays = 0
    dates = generate_dates()

    for date in dates:
        if get_day_from_date(date) == 0:
            numberSundays += 1
        else: pass

    print(numberSundays)

if __name__ == '__main__':
    main()