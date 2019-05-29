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

def date_converter(Startdate):
    week_day = {0: "Monday",1: "Tuesday",2: "Wednesday",3: "Thursday",4: "Friday",5: "Saturday",6: "Sunday"}
    if Startdate is 'NaN':
        pass
    else:
        datee, time = Startdate.split(' ')
        month, day, year = datee.split('/')
        hour, minute = time.split(':')
        w_date=datetime(int(year),int(month),int(day),int(hour),int(minute))
        w1=datetime.weekday(datetime(int(year),int(month),int(day),int(hour),int(minute)))
        weekday=week_day[w1]

        with open("Washington_new1.csv", 'a+') as wfile1:
                wfile1.write(month + "\n")
        with open("Washington_new2.csv", 'a+') as wfile2:
                wfile2.write(year + "\n")
        with open("Washington_new3.csv", 'a+') as wfile3:
                wfile3.write(weekday + "\n")

row=0
while row != int(WASHI_D.shape[0]):
    if WASHI_D.ix[row]["Start date"] != "":
        date_converter(WASHI_D["Start date"][row])
    else:
        pass
    wfile4=open("Washington_new4.csv", 'a+')
    wfile4.write(str(float(WASHI_D["Duration (ms)"][row])/(60*1000))+ "\n")
    wfile4.close()
    wfile5=open("Washington_new5.csv", 'a+')
    wfile5.write(WASHI_D["Member Type"][row].replace("Registered","Subscriber").replace("Casual", "Customer") + "\n")
    wfile5.close()
    row=row+1

#with open("Washington_new.csv", 'w+') as wfile:
#    merge1=pandas.DataFrame( columns=['duration', 'month', 'year', 'weekday', 'usertype'])
#    print(merge1)

#with open("Washington_new1.csv", 'r+') as wfile1:
#    lines = wfile1.readlines()


#    wfile_final["duration"]=lines
#    print(wfile_final)

#wfile1=pandas.read_csv("Washington_new1.csv", names=["duration"])
#wfile2=pandas.read_csv("Washington_new2.csv", names=["month"])
#wfile3=pandas.read_csv("Washington_new3.csv", names=["year"])
#wfile4=pandas.read_csv("Washington_new4.csv", names=["weekday"])
#wfile5=pandas.read_csv("Washington_new5.csv", names=["user_type"])

#with open(r"C:\Amit Agrawal\OneDrive\OneDrive - Ericsson AB\Documents\Tutorial\Python Learning\New folder\Washington_new.csv", 'w+') as wfile:
#    wfilea=pandas.read_csv(r"C:\Amit Agrawal\OneDrive\OneDrive - Ericsson AB\Documents\Tutorial\Python Learning\New folder\Washington_new.csv")
merge=pandas.DataFrame(index=[], columns=['duration', 'month', 'year', 'weekday', 'usertype'])
with open("Washington_new1.csv", 'r+') as wfile1:
    lines = wfile1.readlines()
    merge["duration"]=lines
with open("Washington_new2.csv", 'r+') as wfile2:
    lines = wfile2.readlines()
    merge["month"]=lines
with open("Washington_new3.csv", 'r+') as wfile3:
    lines = wfile3.readlines()
    merge["year"]=lines
with open("Washington_new4.csv", 'r+') as wfile4:
    lines = wfile4.readlines()
    merge["weekday"]=lines
with open("Washington_new5.csv", 'r+') as wfile5:
    lines = wfile5.readlines()
    merge["usertype"]=lines
#    merge=pandas.concat([wfile1, wfile2, wfile3, wfile4, wfile5], axis=1)
#    wfile.write(str(merge))
merge.to_csv("Washington_new.csv")
