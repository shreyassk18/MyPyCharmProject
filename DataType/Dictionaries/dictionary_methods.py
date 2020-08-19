dict1 = {'id':123,
         'name':"shreyas",
         'salary':25000.50}

#popitem() - This will randomly selects an item from dictionary and also removes the same
print(dict1.popitem())
print(dict1)

#clear() - this function deletes everything from dictionary
#dict1.clear()
#print(dict1)

#keys() - this will return the keys in dictionary as tuple
print(dict1.keys())

#values() this will return the values in dictionary as tuple
print(dict1.values())

#get(key) - this will return value of passed key and returns none in case key not found
print(dict1.get('id'))
print(dict1.get('salary'))

#pop(key) - this will remove the passed item from the dict
#throws KeyError in case key is not found
print(dict1.pop('name'))
print(dict1)

#update - This method will merge 2 dictionaries (Replaces value of a key if we give duplicate key )
dict2 = {'surname':'kittur',
         'age':27,
         'salary':32000.00}

dict1.update(dict2)
print(dict1)
