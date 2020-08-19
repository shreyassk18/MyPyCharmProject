#Hierarchical - Class B and class C both inherits class A    --> Multiple childs inherits single parent class

class A:
    a,b = 10,20
    def add(self):
        print(self.a+self.b)

class B(A):
    x,y = 100,200
    def mul(self):
        print(self.x*self.y)

class C(A):
    i,j=10,2
    def div(self):
        print(self.i/self.j)

b = B()
b.add()
b.mul()

c = C()
c.add()
c.div()
