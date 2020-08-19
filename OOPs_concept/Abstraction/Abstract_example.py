from abc import ABC,abstractclassmethod

class Animal(ABC):

    @abstractclassmethod
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        print("eats NON_VEG")

class Cow(Animal):
    def eat(self):
        print("eats VEG")

t = Tiger()
t.eat()

c = Cow()
c.eat()