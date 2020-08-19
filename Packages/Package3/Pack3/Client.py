import sys
sys.path.append(r"C:/Users/shreyas.kittur/PycharmProjects/Baisc_Python/Packages/Package3/Pack1")
from Emp_module import Employee

e = Employee(101,"Shreyas","29495.00")
e.dispemp()


sys.path.append(r"C:/Users/shreyas.kittur/PycharmProjects/Baisc_Python/Packages/Package3/Pack2")
from Stud_module import Student

s = Student(1, "Kiran", 12)
s.dispstud()
