#Single - class B inherits class A   --> One child inherits one parent

class A:
    a,b = 10,20
    def add(self):
        print(self.a+self.b)

class B(A):
    x,y = 100,200
    def mul(self):
        print(self.x*self.y)

b = B()
b.add()
b.mul()
