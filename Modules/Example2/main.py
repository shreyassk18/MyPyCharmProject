#if we have multiple modules with the same function name,

#Approach1
#Here the last imported module's function will be called
from bird import *
from animal import *

fly()
color()

#Approach2
from bird import *

fly()
color()

from animal import *

fly()
color()