#We can access private variables outside of the class, indirectly using a method

class MyClass:
    __empid=101

    def getempd(self,empid):
        self.__empid=empid      #empid=self.__empid is different than self.__empid=empid

    def dispempid(self):
        print(self.__empid)

mc = MyClass()
mc.dispempid()  #Displays private variable value

#We can also modify the private variable value
mc.getempd(105)
mc.dispempid()


