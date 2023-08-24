import calendar
#Read a number n and compute n+nn+nnn
a = int(input("enter a number"))
n1= int("%s" %(a))
n2= int("%s%s" %(a,a))
n3= int("%s%s%s" %(a,a,a))
n4= int("%s%s%s%s" %(a,a,a,a))
print(n1 +n2 +n3 +n4) # a+aa+aaa+aaaa

#calender
y=int(input("enter the year"))
m=int(input("enter a month"))
if y>2023 : print("not yet")
else: 
    if y <2023  :
       if m >12:
          print("please enter a valid month")
       else :
          print(calendar.month(y,m))

if y==2023 and m<=6 :
        print(calendar.month(y,m))
else :
        ("not yet")



#date
from datetime import date

current_date = date.today()  # Get the current date
print(current_date)  # Output: YYYY-MM-DD

# Create a custom date
custom_date = date(2022, 12, 31)
print(custom_date)  # Output: 2022-12-31


#time 
from datetime import datetime

current_time = datetime.now().time()
print(current_time)

#time and date

import datetime
from math import pi

now = datetime.datetime.now()
print("Current time and date is:")
print(now.strftime("%y-%m-%d %H:%M:%S"))
#The strftime method is used to format the datetime object as a string to the specified format string.


