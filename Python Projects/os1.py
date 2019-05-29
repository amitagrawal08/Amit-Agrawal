import os
import shutil
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # make a duplicate of an existing file
	if path.exists("guru99.txt"):
    # get the path to the file in the current directory
            src=path.realpath("guru99.txt");
	#seperate the path from the filter
            head, tail = path.split(src)
            print("path:" +head)
            print("file:" +tail)
	#let's make a backup copy by appending "bak" to the name
            dst = src+".bak"
	# nowuse the shell to make a copy of the file
            shutil.copy(src, dst)
	#copy over the permissions,modification
            shutil.copystat(src,dst)
main()

def main1():
    # Get the modification time
    t = time.ctime(path.getmtime("guru99.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("guru99.txt")))
main1()

#os.rename("guru99.txt","career.guru99.txt")
