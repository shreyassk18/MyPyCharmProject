#approach1
list1 = [x for x in range(10)]
print(list1)

#approach2
list1 = [x+1 for x in range(10)]
print(list1)

#even numbers
list1 = [x for x in range(10) if x%2 == 0]
print(list1)

#odd numbers
list1 = [x for x in range(10) if x%2 != 0]
print(list1)