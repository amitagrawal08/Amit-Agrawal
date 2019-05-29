import pandas
import os
import datetime
from datetime import datetime
from datetime import time
from datetime import *
from datetime import date
import timestring

CHICA_S = pandas.read_csv(r"C:\Python\Project1\data\Chicago-2016-Summary.csv")
CHICA_D = pandas.read_csv(r"C:\Python\Project1\data\Chicago-Divvy-2016.csv")
NYC_S = pandas.read_csv(r"C:\Python\Project1\data\NYC-2016-Summary.csv")
NYC_D = pandas.read_csv(r"C:\Python\Project1\data\NYC-CitiBike-2016.csv")
WASHI_S = pandas.read_csv(r"C:\Python\Project1\data\Washington-2016-Summary.csv")
WASHI_D = pandas.read_csv(r"C:\Python\Project1\data\Washington-CapitalBikeshare-2016.csv")
print(CHICA_S.shape)
print(CHICA_D.shape)
print(NYC_S.shape)
print(NYC_D.shape)
print(WASHI_S.shape)
print(WASHI_D.shape)

print(CHICA_S.columns)
print(NYC_S.columns)
print(WASHI_S.columns)
print(CHICA_D.columns)
print(NYC_D.columns)
print(WASHI_D.columns)

########################## String to Datetime formatting using strptime method ###############
#WASH_SD = datetime.strptime(WASHI_D["Start date"][0], '%m/%d/%Y %H:%M')
#print(WASH_SD.year, WASH_SD.month, WASH_SD.day, WASH_SD.hour, WASH_SD.minute)
#################################################
########################## String to Datetime formatting using split method ###############
#week_day = {0: "Monday",1: "Tuesday",2: "Wednesday",3: "Thursday",4: "Friday",5: "Saturday",6: "Sunday"}
#datee, time = WASHI_D["Start date"][0].split()
#month, day, year = datee.split('/')
#hour, minute = time.split(':')
#print(datee, time, year, month, day, hour, minute)
#w1=datetime.weekday(datetime(int(year),int(month),int(day),int(hour),int(minute)))
#weekday=week_day[w1]
#print(weekday)
#########################
#def date_converter(date):
#    return timestring.Date(WASHI_D["Start date"])

def date_converter(Startdate):
    return timestring.Date(Startdate)
row=0
while row != int(WASHI_D.shape[0]):
#    print(row)

#print(type(WASHI_D["Start date"]))
#for stdate in WASHI_D["Start date"]:
#    print(stdate)
#    print(type(stdate))
#    if stdate == '':
#        WASHI_D.replace(stdate,"")
#    else:
#        stdate_new=date_converter(stdate)
#        WASHI_D.replace(stdate,stdate_new)

    if WASHI_D.ix[row]["Start date"] != "":
        stdate_new=date_converter(WASHI_D["Start date"][row])
    else:
        stdate_new=" "
    WASHI_D.set_value(row, "Start date", stdate_new)
    print(WASHI_D.ix[row]["Start date"])
    with open("Washington_new.csv", 'w') as w_new:
        w_new.write(stdate_new.day)
    WASHI_D.to_csv(r"Washington_new.csv", index=False, encoding='utf8')
    row=row+1
print(WASHI_D.loc[: ,"Start date":"End date"])
