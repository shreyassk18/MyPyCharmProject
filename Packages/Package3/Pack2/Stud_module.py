class Student:
    def __init__(self,rollno,name,grade):
        self.rno = rollno
        self.name = name
        self.grd = grade

    def dispstud(self):
        print("RollNo:{} Name:{}  Grade:{}".format(self.rno,self.name,self.grd))


