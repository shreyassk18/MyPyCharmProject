class Employee:
    def __init__(self,eid,ename,sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def dispemp(self):
        print("empid:{} empname:{}  salary:{}".format(self.eid,self.ename,self.sal))
