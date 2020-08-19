#when we create an object without a reference, it is called as nameless object

class MyClass:
    def myFunc(self):
        pass
    def display(self,name):
        print("Name is :", name)

mc = MyClass()      #named object
mc.myFunc()
mc.display("Shreyas")

MyClass().display("Kittur") #nameless object