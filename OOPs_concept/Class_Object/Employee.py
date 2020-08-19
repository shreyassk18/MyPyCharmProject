class Emp:
    def __init__(self,eid,ename,sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def display(self):
        print("Employee id:{}  Employee name:{}  Salary:{}".format(self.eid,self.ename,self.sal))
        print("Employee id:%d  Employee name:%s  Salary:%g" %(self.eid,self.ename,self.sal))

e = Emp(101,"Shreyas",30000.50)
e.display()
        