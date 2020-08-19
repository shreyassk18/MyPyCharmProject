#Approach1
import module1

module1.add(10,20)
module1.mul(10,20)

#Approach2
from module1 import add,mul     #if we dont want to use module name each time while calling a function

add(10,20)
mul(10,20)

#Approach3
from module1 import *       #When we have too many numbers of functions in a module and we want to import all functions

add(10,20)
mul(10,20)
