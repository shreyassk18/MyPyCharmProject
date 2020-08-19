#Instance methods we can directly call using class object.

#In python we have only static methods, not static variables
#We have to use @staticmethod keyword to define a static method.
#We can call a static method using class name.
#By default static methods will not have any parameters
#If we have self parameter in static method, that will be treated as an argument.

class Demo:
    def m1(self):
        print("Instance method")

    @staticmethod
    def m2():
        print("static method")

d = Demo()
d.m1()
Demo.m2()

#Static methods with parameter
class Demo1:
    def m3(self):
        print("Instance method")

    @staticmethod
    def m4(self):
        print(self)
Demo1.m4(10)



