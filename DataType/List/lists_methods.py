list1 = [2,4,7,1,4,10,11,3]

#append
list1.append(19)    #adds 19 at the end of list
print(list1)

#count
print(list1.count(4)) # number of times 4 is presnt in the list

#extend list1
list2 = [99,86]
list1.extend(list2) # Adds 99 and 86 to list1 at end
print(list1)

#index
print(list1.index(4))   #This will return the index of value 4

#insert a value at perticular index
list1.insert(1,23)  #1 is index, 23 is a value
print(list1)

#pop (remove perticular value and returns it)
list1.pop(1)    #here value 1 is the index
print(list1)

#remove
list1.remove(86)
print(list1)

#reverse
list1.reverse()
print(list1)

#sort
list1.sort()
print(list1)

#Copy a list into another list
list_copy=list(list1)
print(list_copy)