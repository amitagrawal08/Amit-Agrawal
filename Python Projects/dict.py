Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print((Dict['Tiffany']))

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
studentX=Boys.copy()
studentY=Girls.copy()
print(studentX)
print(studentY)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Dict.update({"Sarah":9})
print(Dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
del Dict ['Charlie']
print(Dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Students Name: %s" % list(Dict.items()))

Dict = {'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim':18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in list(Boys.keys()):
    if key in list(Dict.keys()):
        print(True)
    else:
        print(False)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict.keys())
print(Students)
Students.sort()
for S in Students:
    print(":".join((S,str(Dict[S]))))


    Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
    print(len(Dict))
    print("Length : %d" % len (Dict))

    Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
    print(type(Dict))
    print ("variable Type: %s" %type (Dict))

Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
#print(cmp(Girls, Boys))

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("printable string:%s" % str (Dict))
