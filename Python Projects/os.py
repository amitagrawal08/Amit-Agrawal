import os.path
from os import path

def main():
   print ("file exist:" + str(path.exists('guru99.txt')))
   print ("File exists:" + str(path.exists('career.guru99.txt')))
   print ("directory exists:" + str(path.exists('New folder')))
main()

def main1():
	print ("Is it File?" + str(path.isfile('guru99.txt')))
	print ("Is it File?" + str(path.isfile('New folder')))
main1()

def main2():
    print ("Is it Directory?" + str(path.isdir('guru99.txt')))
    print ("Is it Directory?" + str(path.isdir('New folder')))
main2()
