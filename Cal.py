
'''This work is done by Sprihanjay Banik. 
   Email- sbanik1@student.gsu.edu. 
   PantherID - 002706373'''


import sys

month = int(sys.argv[1])
year = int(sys.argv[2])


# Creating list of months 
name_of_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# Creating list of days in months
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Changing days in february for leap year
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    days_in_month[1] = 29
else:
    days_in_month[1] = 28


# Exceptions/User input error
if month <= 0 or month > 12:
    raise Exception("month must be in 1...12")
if year <= 0:
    raise Exception("year", year,"is out of scope")
#For extra credit changing default Exceptions

# Determining day of week for the first of the month
from datetime import date

d = date(year,month,1)
day_of_week = (d.weekday()+1)%7


# Outputting Calender
# Since index of first month is 0 in list, we need to subtract 1 from user input to get desired index. 
print(" "*((20-len(name_of_month[month - 1])-5)//2),name_of_month[month - 1],year)

print("Su Mo Tu We Th Fr Sa")

for i in range(1, days_in_month[month-1] + 1):
        if i == 1:
            print((' ' * 3) * day_of_week, end='')
        if i < 10:
            print('', i, end=' ')
        elif i >= 10:
            print(i, end=' ')
        if (i + day_of_week) % 7 == 0:
            print('\n', end='')


# Task left : Error messages and centering the months