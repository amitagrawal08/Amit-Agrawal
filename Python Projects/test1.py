import pandas
import os
import csv
import datetime
from datetime import datetime
from datetime import time
from datetime import *
from datetime import date
import timestring
import numpy
import shutil
import os.path
import string

if os.path.isfile("Washington_new1.csv"):
    os.remove("Washington_new1.csv")
if os.path.isfile("Washington_new2.csv"):
    os.remove("Washington_new2.csv")
if os.path.isfile("Washington_new3.csv"):
    os.remove("Washington_new3.csv")
if os.path.isfile("Washington_new4.csv"):
    os.remove("Washington_new4.csv")
if os.path.isfile("Washington_new5.csv"):
    os.remove("Washington_new5.csv")
if os.path.isfile("Washington_new.csv"):
    os.remove("Washington_new.csv")

WASHI_D=pandas.read_csv(r"C:\Python\Project1\data\Test.csv", header=0, sep=",")
#print(WASHI_D["Start date"])
def date_converter(Startdate):
#    return timestring.Date(Startdate)
    week_day = {0: "Monday",1: "Tuesday",2: "Wednesday",3: "Thursday",4: "Friday",5: "Saturday",6: "Sunday"}
    if Startdate is 'NaN':
        pass
    else:
        datee, time = Startdate.split(' ')
        month, day, year = datee.split('/')
        hour, minute = time.split(':')
#    print(datee, time, year, month, day, hour, minute)
        w_date=datetime(int(year),int(month),int(day),int(hour),int(minute))
        w1=datetime.weekday(datetime(int(year),int(month),int(day),int(hour),int(minute)))
        weekday=week_day[w1]
#        return w_date, weekday

        with open("Washington_new1.csv", 'a+') as wfile1:
                wfile1.write(month + "\n")
        with open("Washington_new2.csv", 'a+') as wfile2:
                wfile2.write(year + "\n")
        with open("Washington_new3.csv", 'a+') as wfile3:
                wfile3.write(weekday + "\n")
row=0
while row != int(WASHI_D.shape[0]):
#    print(row)
#    for stdate in WASHI_D["Start date"]:
#        print(stdate)
#        if stdate == '':
#            pass
#        else:
#    print(WASHI_D.ix[row]["Start date"])
    if WASHI_D.ix[row]["Start date"] != "":
#    if WASHI_D.loc[row,"Start date"] is NaN
        date_converter(WASHI_D["Start date"][row])
#        stdate_new=date_converter(WASHI_D["Start date"][row])
#        print(stdate_new)
    else:
#        stdate_new=" "
        pass
#    WASHI_D.ix[row]["Start date"] = stdate_new
#            A=WASHI_D.ix[row]["Start date"]==stdate_new
#            print(A)
#    print(WASHI_D.tail(2))
#            file_update=csv.writer(open(r"C:\Python\Project1\data\Test.csv", "w"))
#            file_update.write(stdate_new)
#            WASHI_D["Start date"][row]=str(stdate_new)
#        print(WASHI_D["Start date"])
##    WASHI_D.set_value(row, "Start date", stdate_new)
##    print(WASHI_D.ix[row]["Start date"])
##    W_month=WASHI_D.ix[row]["Start date"].month()
#    WASHI_D.to_csv("Test.csv", index=False, encoding='utf8')
    wfile4=open("Washington_new4.csv", 'a+')
    wfile4.write(str(float(WASHI_D["Duration (ms)"][row])/(60*1000))+ "\n")
    wfile4.close()
    wfile5=open("Washington_new5.csv", 'a+')
    wfile5.write(WASHI_D["Member Type"][row].replace("Registered","Subscriber").replace("Casual", "Customer") + "\n")
    wfile5.close()
    row=row+1

wfile1=pandas.read_csv("Washington_new1.csv", names=["duration"])
#wfile1.columns=['duration']
wfile2=pandas.read_csv("Washington_new2.csv", names=["month"])
#wfile2.columns=['month']
wfile3=pandas.read_csv("Washington_new3.csv", names=["year"])
#wfile3.columns=['year']
wfile4=pandas.read_csv("Washington_new4.csv", names=["weekday"])
#wfile4.columns=['weekday']
wfile5=pandas.read_csv("Washington_new5.csv", names=["user_type"])
#wfile5.columns=['user_type']
#wfile=pandas.merge(wfile1,wfile2,wfile3,wfile4,wfile5)
with open("Washington_new.csv", 'a+') as wfile:
    merge=pandas.concat([wfile1, wfile2, wfile3, wfile4, wfile5], axis=1)
    wfile.write(str(merge))
print(wfile)

#merged=pandas.concat(wfile1, wfile2, wfile3, wfile4, wfile5)
#merged.to_csv('Washington_new.csv', index=None, header=None)

#print(type("Washington_new1"))
#print(type("Washington_new2"))
#print(type("Washington_new3"))
#print(type("Washington_new4"))
#print(type("Washington_new5"))

#print(WASHI_D.loc[: ,"Start date":"End date"].tail(2))
#print(type(WASHI_D["Start date"]))
#print(WASHI_D.loc[: ,"Start date":"End date"])
