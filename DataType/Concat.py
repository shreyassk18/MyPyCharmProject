#Concatination is possible only if both types are same
#Valid cases

print(10+10)
print(10.5+10.5)
print("welcome"+"shreyas")
print(10+10.5)
print(True+5)
print(True+True)
print(False+10)

#Invalid cases

print(10+"welcome")     #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(10.5+"welcome")   #TypeError: unsupported operand type(s) for +: 'float' and 'str'
print(True+"welcome")   #TypeError: unsupported operand type(s) for +: 'bool' and 'str'
