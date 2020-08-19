#Multilevel - class C inherits class B, class B inherits class A --> One child inherits another child, and another child inherits parent
#we can create any number of levels

class A:
    a,b = 10,20
    def add(self):
        print(self.a+self.b)

class B(A):
    x,y = 100,200
    def mul(self):
        print(self.x*self.y)

class C(B):
    i,j=10,2
    def div(self):
        print(self.i/self.j)

c = C()
c.add()
c.mul()
c.div()