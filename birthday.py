"""
birthday.py
Author: Earl
Credit: None
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name=input("Hello,  what is your name? ")

month=input("Hi " +name+", what was the name of the month you were born in? ")

year=input("And what year were you born in, " +name+ "? ")

day=input("And the day? ")

if month in ["June", "July", "August"] and year <1980:
    print(+name+ ", you are a summer baby of the stone age.")
    
if month in ["June", "July", "August"] and year >1980 and year <=1990:
    print(+name+ ", you are a summer baby of the eighties.")
    
if month in ["June", "July", "August"] and year >1990 and year <=2000:
    print
    
if month in ["June", "July", "August"] and year >2000:
    print(+name+ ", you are a summer baby of the two thousands.")
    
    
if month in ["September", "October", "November"] and year <1980:
    print(+name+ ", you are a fall baby of the stone age.")
    
if month in ["September", "October", "November"] and year >1980 and year <1990:
    print(+name+ ", you are a fall baby of the eighties.")
    
if month in ["September", "October", "November"] and year >1990 and year <2000:
    print(+name+ ", you are a fall baby of the nineties.")
    
if month in ["September", "October", "November"] and year >2000:
    print(+name+ ", you are a fall baby of the two thousands.")
    
    
if month in ["December", "January", "February"] and year <1980:
    print(+name+ ", you are a winter baby of the stone age.")
    
if month in ["December", "January", "February"] and year >1980 and year <1990:
    print(+name+ ", you are a winter baby of the eighties.")
    
if month in ["December", "January", "February"] and year >1990 and year <2000:
    print(+name+ ", you are a winter baby of the nineties.")
    
if month in ["December", "January", "February"] and year >2000:
    print(+name+ ", you are a winter baby of the two thousands.")