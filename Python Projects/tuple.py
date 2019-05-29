Tup = ('Jan','feb','march')
tup1 = ();
Tup1 = (50,);
tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print(tup1[0])
print(tup2[1:4])

## Packing and Unpacking
x = ("Guru99", 20, "Education")    # tuple packing
print(x)
(company, emp, profile) = x    # tuple unpacking
print(x)
print(company)
print(emp)
print(profile)

a=(5,6)
b=(1,4)
if (a>b):print("a is bigger")
else: print("b is bigger")

a=(5,6)
b=(5,4)
if (a>b):print("a is bigger")
else: print ("b is bigger")

a=(5,6)
b=(6,4)
if (a>b):print("a is bigger")
else: print("b is bigger")

a = {'x':100, 'y':200}
b = list(a.items())
print(b)
