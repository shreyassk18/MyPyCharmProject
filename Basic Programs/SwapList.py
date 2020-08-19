#Swapping first and last element of a list
mylist = [12, 6, 8, 32, 78, 9]
print("mylist before swapping", mylist)

#Approach1 using temproary variable
# s = len(mylist)
#
# temp = mylist[0]
# mylist[0]= mylist[s-1]  #Because len functions counts from 1 but index will start from 0 so s value will be 5
# mylist[s-1] = temp
#
# print("mylist after swapping",mylist)

#Approach2
# mylist[0],mylist[-1] = mylist[-1],mylist[0] #-1 represnt last index of a list
#
# print("mylist after swapping",mylist)

#Approach3 : using tuple
# get = (mylist[-1], mylist[0])   #This is called packing
# mylist[0], mylist[-1]=get
# print("mylist after swapping",mylist)

#Approach4 : using * operand
# start,*middle,end=mylist
#
# print(start)
# print(middle)
# print(end)
#
# mylist=[end,*middle,start]
# print("mylist after swapping",mylist)

#Approach5 :
first = mylist.pop(0)   #It contains value of index 0 (first element)
last= mylist.pop(-1)    #It contains value of index -1 (last element)

mylist.insert(0,last)   #Inserting last element value to index 0
mylist.append(first)    #appending first element value at the end of list

print("mylist after swapping",mylist)