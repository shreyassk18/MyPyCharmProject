import sys
sys.path.append(r"C:/Users/shreyas.kittur/PycharmProjects/Baisc_Python/Packages/Package1/Pack1")

#Approach1 for accessing pack1 modules
import module1
import module2

module1.display()
module2.show()

#Approach2
from module1 import *
from module2 import *

display()
show()
