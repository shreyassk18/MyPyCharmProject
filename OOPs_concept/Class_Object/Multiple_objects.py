#Each objects of a class will be occupying different memory location

class MyClass:
    def display(self):
        print("Hello..!! Welcome to python")

obj1 = MyClass()
obj1.display()

obj2 = MyClass()
obj2.display()