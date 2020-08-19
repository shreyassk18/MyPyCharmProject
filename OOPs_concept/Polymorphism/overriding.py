#Overriding means having same name for variable or method but can be used for different functionalities

#overriding variable
'''
class parent:
    name = "Shreyas"

class child(parent):
    name = "Pavan"

a = child()
print(a.name)   #This will print the latest value of the name
'''

class parent:
    name = "Shreyas"

class child(parent):
    pass

a = child()
print(a.name)   #Thid will print the value from parent class

#overriding method
class Bank:
    def rate_of_interest(self):
        return 0

class ICICI():
    def rate_of_interest(self): #overriding parent class method.
        return 10.5

obj = ICICI()
print(obj.rate_of_interest())

obj1 = Bank()
print(obj1.rate_of_interest())