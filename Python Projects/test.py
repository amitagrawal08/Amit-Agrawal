import pandas
import os
import datetime
from datetime import datetime
from datetime import time
from datetime import *
from datetime import date
import timestring

#WASHI_D =open(r"C:\Python\Project1\data\Test.csv", 'r+').read()
#read.seek()
#print(WASHI_D)
WASHI_D=pandas.read_csv(r"C:\Python\Project1\data\Test.csv", header=0, sep=",")
#print(WASHI_D["Start date"])
#print(WASHI_D.head(3))
#print(type(WASHI_D["Start date"]))

#with open(WASHI_D,'r+') as file1:
#    print(type(TEST["Start date"]))
#    content=file1.read()
#    print(type(content))
#    print(TEST["Start date"])
#    WASHI_D1=file1["Start date"]
#    print(type(WASHI_D1))
def date_converter(Startdate):
    return timestring.Date(Startdate)
#    return datetime.strptime(Startdate, '%m/%d/%Y %H:%M')
#    week_day = {0: "Monday",1: "Tuesday",2: "Wednesday",3: "Thursday",4: "Friday",5: "Saturday",6: "Sunday"}
#    datee, time = Startdate.split()
#    month, day, year = datee.split('/')
#    hour, minute = time.split(':')
#    print(datee, time, year, month, day, hour, minute)
#    w1=datetime(int(year),int(month),int(day),int(hour),int(minute))
#    weekday=week_day[w1]
#    return w1

row=0
while row != int(WASHI_D.shape[0]):
    print(row)
    for stdate in WASHI_D["Start date"]:
#        print(stdate)
        if stdate == '':
            pass
##        WASHI_D["Start date"].replace(stdate,"")
        else:
            stdate_new=date_converter(stdate)
            print(stdate_new)
#            print(WASHI_D.set_value(row, "Start date", stdate_new))
            WASHI_D.loc[WASHI_D["Start date"][row]]=stdate_new
#            file_update=csv.writer(open(r"C:\Python\Project1\data\Test.csv", "w"))
#            file_update.write(stdate_new)
#            WASHI_D["Start date"][row]=str(stdate_new)
#        print(WASHI_D["Start date"])
    row=row+1
