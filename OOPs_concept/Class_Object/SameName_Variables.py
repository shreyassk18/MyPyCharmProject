#Using same names for local,class and global variables
#We have to use globals() method if variable names are same

a,b=10,20   #Global variables
class MyClass:

    a,b=100,200       #Class variables

    def add(self,a,b):  #Local variables
        print(a+b)  #This will access local variables
        print(self.a+self.b)   #To use class variables inside a method, we need to use self keyword
        print(globals()['a']+globals()['b'])    #Accessing global variables

mc = MyClass()
mc.add(300,400)     #Passing local variable values