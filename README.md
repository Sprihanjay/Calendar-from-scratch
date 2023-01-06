# Calendar-from-scratch
Creating a Calendar from scratch without importing any module. (CSC 1301 Projects)
#### Calendar

A Python program that reads two command line parameters, month (between 1 and 12) and year (between 1 and 9999), and produces the calendar for specified month in the specified year. The format of the calendar is given in the sample runs shown later.

1.  To read command line parameters, you can use the folowing code:
    
    import sys
    
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    
2.  To determine day of week for the first of the month, you can use the following code:
    
    from datetime import date
    
    d = date(year,month,1)
    day_of_week = (d.weekday()+1)%7
    
3.  To catch errors in input you should use the try-except statement as follows:
    
    try:
      month = int(sys.argv[1])
      year = int(sys.argv[2])
      ...
      ...
    except Exception as e:
      print(str(e))
    

Here are some sample runs of the program:

Mac-mini:cal sb$ python3 Cal.py 7 2022
<pre>
     July 2022
Su Mo Tu We Th Fr Sa
                1  2 
 3  4  5  6  7  8  9 
10 11 12 13 14 15 16 
17 18 19 20 21 22 23 
24 25 26 27 28 29 30 
31 </pre>

Mac-mini:cal sb$ python3 Cal.py 10 1958
<pre>
    October 1958
Su Mo Tu We Th Fr Sa
          1  2  3  4 
 5  6  7  8  9 10 11 
12 13 14 15 16 17 18 
19 20 21 22 23 24 25 
26 27 28 29 30 31 
</pre>

Mac-mini:cal sb$ python3 Cal.py 15 2022
month must be in 1..12

Mac-mini:cal sb$ python3 Cal.py 10 20022
year 20022 is out of range

Mac-mini:cal sb$ python3 Cal.py abc 2022
invalid literal for int() with base 10: 'abc'

Mac-mini:cal sb$ python3 Cal.py 10 2022a
invalid literal for int() with base 10: '2022a'

Mac-mini:cal sb$ python3 Cal.py 10
list index out of range

Mac-mini:cal sb$ python3 Cal.py
list index out of range
