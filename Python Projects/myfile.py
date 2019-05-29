def test_1(a):
    if a==2:
        print("Hello")
    else:
        print("test")
print(test_1(2))

numbers=[1,2,3]
file = open("Number.txt", "w")
for item in numbers:
    file.write(str(item) + "\n")
file.close()
myfile = open("Test.txt", "a+")
myfile.read()
myfile.write("\nAmit1")
myfile.close()
