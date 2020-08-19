list1=[2,3,4,1,32]

print(2 in list1)
print(32 not in list1)
print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))
print(list1[1:3])
print(list1[:7])

# + opeartor joins the two lists
# * opeartors repeats the list

list2=[1,2]
list3=[4,5]
list4=list2 + list3
print(list4)

list5=[6,7,8,9]
list6=list5 * 3
print(list6)

#Traversing lists
list7=[1,2,3,4,5]
for i in list7:
    print(i)
