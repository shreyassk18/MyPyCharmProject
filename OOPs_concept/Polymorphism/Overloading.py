#Defining different parameter values for a same method is called overloading

#Example 1:
class Human:
    def sayHello(self,name=None):
        if name is not None:
            print("Hello " +name)
        else:
            print("Hello")

obj = Human()
obj.sayHello()
obj.sayHello("Shreyas")

#Example 2:
class Bird:
    def fly(self, name=None):
        if name == "Parrot":
            print(name, "can fly")
        elif name == "Penguine":
            print(name, "cannot fly")
        elif name is None:
            print("No input")
        else:
            print("Wrong input")

b = Bird()
b.fly()
b.fly("Parrot")
b.fly("Penguine")
b.fly("Humming")

