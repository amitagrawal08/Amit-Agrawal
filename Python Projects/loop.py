#
#Example file for working with loops
#
def main():
#	x=0
	#define a while loop
#	while(x <4):
#		print(x)
#		x = x+1
    #Define a for loop
  for x in range(2,7):
    		print(x)
main()

def main():
	#use a for loop over a collection
	Months = ["Jan","Feb","Mar","April","May","June"]
	for m in Months:
		print(m)

if __name__ == "__main__":
	main()

def main():
# use the break and continue statements
  	for x in range (10,20):
  		#if (x == 15): break
#      if (x % 5 == 0) : continue
  		print(x)
main()

def main():
# use the break and continue statements
		for x in range (10,20):
			#if (x == 15): break
			   if (x % 5 == 0) : continue
			   print(x)
main()

def main():
	#use a for loop over a collection
	Months = ["Jan","Feb","Mar","April","May","June"]
	for i, m in enumerate (Months):
		print(i,m)
main()

i=0
for i in '50':
 print ("guru99",i)
