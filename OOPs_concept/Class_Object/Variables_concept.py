#Local variables - Created inside a method  (Can be accessed only by methods defined)
#class variables - Created within a class   (Can be accessed by methods within a class)
#global variables - Created outside class (Can be accessed globally by all methods and classes)

i,j=10,20   #Global variables
class MyClass:

    a,b=100,200       #Class variables

    def add(self,x,y):  #Local variables
        print(x+y)
        print(self.a+self.b)   #To use class variables inside a method, we need to use self keyword
        print(i+j)

mc = MyClass()
mc.add(300,400)     #Passing local variable values