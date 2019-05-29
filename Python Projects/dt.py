from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from datetime import tzinfo

def main():
    today = date.today()
    print("Today's date is: ", today)
    print("Today's date is: ", today.day)
    print("Today's month is: ", today.month)
    print("Today's year is: ", today.year)
    print("Today's weekday is: ", today.weekday())
main()

today1=datetime.now()
print("Current date and time is: " , today1)

print(datetime.date(today1))
print(datetime.time(today1))
print(datetime.weekday(today1))
print(datetime.tzname(today1))

wd=datetime.weekday(datetime.now())
#Days start at 0 for monday
days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print("Today is day number %d" % wd)
print("which is a " + days[wd])


#Example file for formatting time and date output
#
from datetime import datetime
def main():
   #Times and dates can be formatted using a set of predefined string
   #Control codes
      now= datetime.now() #get the current date and time
      #%c - local date and time, %x-local's date, %X- local's time
      print(now.strftime("%c"))
      print(now.strftime("%x"))
      print(now.strftime("%X"))
##### Time Formatting ####
      #%I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
      print(now.strftime("%I:%M:%S %p")) # 12-Hour:Minute:Second:AM
      print(now.strftime("%H:%M")) # 24-Hour:Minute

main()

# construct a basic timedelta and print it
print (timedelta(days=365, hours=8, minutes=15))
# print today's date
print ("today is: " + str(datetime.now()))
# print today's date one year from now
print ("one year from now it will be:" + str(datetime.now() + timedelta(days=365)))
# create a timedelta that uses more than one argument
print ("in one week and 4 days it will be " + str(datetime.now() + timedelta(weeks=1, days=4)))
# How many days until New Year's Day?
today = date.today()  # get todays date
print(today)
nyd = date(today.year, 1, 1) + timedelta(days=365) # get New Year Day for the same year
print(nyd)
if nyd > today:
    print ("New Year day will come after %d days " % ((nyd - today).days))

# How many days until New Year's Day?
today = date.today()  # get todays date
nyd = date(today.year, 1, 1)  # get New Year Day for the same year
# use date comparison to see if New Year Day has already gone for this year
# if it has, use the replace() function to get the date for next year
if nyd < today:
    print ("New Year day is already went by %d days ago" % ((today - nyd).days))

today = date.today()
#format= datetime.strptime("2018:12:23", "%Y:%m:%d")
#print(format)
