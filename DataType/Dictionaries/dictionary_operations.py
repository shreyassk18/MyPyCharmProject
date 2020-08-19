# == and != operators tells whether dict contains same items or not
#we cannot use other relational operators on dict as >,<,etc...

dict1 = {'id':123, 'name':"shreyas"}
dict2= {'id':456, 'name':"pavan"}

dict3 = {'id':123, 'name':"shreyas"}
dict4= {'name':"shreyas", 'id':123}

print(dict1 == dict2)
print(dict3 == dict4)   #order is not important, whether the element is present in the dict is important


print(dict1 != dict2)
print(dict3 != dict4)


