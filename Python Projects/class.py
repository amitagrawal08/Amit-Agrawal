# Example file for working with classes
class myClass():
  def method1(self):
      print("Guru99")

  def method2(self,someString):
      print("Software Testing:" + someString)


def main():
  # exercise the class methods
  c = myClass ()
  c.method1()
  c.method2(" Testing is fun")

if __name__== "__main__":
  main()


  # Example file for working with classes
  class myClass():
    def method1(self):
        print("Guru99")

    def method2(self,someString):
        print("Software Testing:" + someString)

  class childClass(myClass):
    def method1(self):
          #myClass.method1(self);
          print ("Child Class Method1")

    def method2(self):
          print("childClass method2")

    def method3(self,someString):
          print("Software Testing childClass:" + someString)


  def main():
    # exercise the class methods
    c2 = childClass()
    c2.method1()
    c2.method2()
    c2.method3(" Amit")

  if __name__== "__main__":
    main()

    class User:
        name = ""

        def __init__(self, name):
            self.name = name

        def sayHello(self):
            print("Welcome to Guru99, " + self.name)

    User1 = User("Alex")
    User1.sayHello()
