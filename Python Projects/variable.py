f = 101;
print(f)
# Global vs.local variables in functions
def someFunction():
  global f
print(f)
f = "changing global variable"
someFunction()
print(f)

g = 11;
print(g)
del g
print(g)
