class MyClass:
    def demo(self):
        pass
o1=MyClass()
o2=MyClass()
o3=o1

#Find memory location of objects
print(id(o1))
print(id(o2))
print(id(o3))

#Check if objects have same memory location
print(o1 is o2)
print(o1 is o3)

print(o1 is not o2)
print(o1 is not o3)
