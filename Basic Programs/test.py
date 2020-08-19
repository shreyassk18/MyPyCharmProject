#Example1
import random

list = [1,2,3,4,5,67,56,38,93,5,76,45]
random.shuffle(list)
print(list)

#Example2
list1 = ["1", "4", "3", "2", "6"]

list1 = [int(i) for i in list1] #Converts strings to int

list1.sort()
print(list1)

#Example3
import time
localtime = time.asctime(time.localtime(time.time()))   #Fetch current time
print(localtime)