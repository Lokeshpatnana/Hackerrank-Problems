""" 
Jack is always excited about sunday. It is favourite day, when he gets to play all day. And goes to cycling with his friends.

So every time when the month starts he counts the number of sundays he will get to enjoy.
Considering the month can start with any day, be it Sunday, Monday...Or so on.

Count the number of Sunday jack will get with in n number of days.
"""

start_day = input("Enter Start day of Month:")
days = int(input("Enter Number of Days:"))
sundays = 0

d = {'sun':1,'mon':2,'tue':3,'wed':4,'thu':5,'fri':6,'sat':7}

sundays = sundays + days // 7
mod = days % 7
for i in range(d[start_day],d[start_day] + mod):
    if (i > 7):
        if ((i - 7) == 1):
            sundays += 1
    elif (i <= 7):
        if (i == 1):
            sundays += 1
print(sundays)