from abc import ABC,abstractmethod

class Cal(ABC):
    def __init__(self, value):  #constructor
        self.value=value    #making value variable as a class variable, so that we can access the same in sub-classes and methods

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

class C(Cal):
    def add(self):
        print(self.value+100)

    def sub(self):
        print(self.value-50)

c = C(100)  #__init__ constructor will be invoked when we create object for a class
c.add()
c.sub()