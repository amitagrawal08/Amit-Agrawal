#
#Example file for working with conditional statement
#
def main():
	x,y =2,8

	if(x < y):
		st= "x is less than y"
	print(st)

#if __name__ == "__main__":
main()


def main():
	x,y = 10,8
	st = "x is less than y" if (x < y) else "x is greater than or equal to y"
	print(st)

if __name__ == "__main__":
	main()

def SwitchExample(argument):
      switcher = {
          0: " This is Case Zero ",
          1: " This is Case One ",
          2: " This is Case Two ",
      }
      return switcher.get(argument, "nothing")

print (SwitchExample(1))
