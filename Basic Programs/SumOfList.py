#Approach1
mylist = [5,10,20,15,10]
total=1

for i in range(0,len(mylist)):
    total=total*mylist[i]

print("Product of all elements given in a list is:",total)

#Approach2
print("Sum of all elements given in a list is:",sum(mylist))

