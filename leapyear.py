def leapYear(year):

    if year % 4 == 0:
        return '{} is a leap year'.format(year)
    else:
        return '{} is not a leap year'.format(year)

year = int(input('Type a year: '))
print(leapYear(year))
