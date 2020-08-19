#Multiple - Class C inherits both Class A and class B    --> Single child inherits multiple parent class

class A:
    a,b = 10,20
    def add(self):
        print(self.a+self.b)

class B:
    x,y = 100,200
    def mul(self):
        print(self.x*self.y)

class C(A,B):
    i,j=10,2
    def div(self):
        print(self.i/self.j)
c = C()
c.add()
c.mul()
c.div()
