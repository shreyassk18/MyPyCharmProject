#Dictionary is a python data type used to store a key value parameter
#It enables you to quickly retrieve,add,remove,modify, values using key
#It is similar to hash map in java
#These are mutable
#each key in the dictionary must be unique

dict1 = {'id':123, 'name':"shreyas"}
print(dict1)

#retrieve specific element
print(dict1['id'])

#add new element
dict1['salary']="10500.50"
print(dict1)

#modify existing element
dict1['salary']="20500.50"
print(dict1)

#delete perticular element
del dict1['salary']
print(dict1)

#length
print(len(dict1))
