tuple = (1,2,3,4,5,6)
print(tuple)

print(min(tuple))
print(max(tuple))
print(len(tuple))
print(sum(tuple))

#traversing tuple
for i in tuple:
    print(i, end=" ")

print("\n")
#slicing tuple
print(tuple[1:4])
print(tuple[:5])
print(tuple[3:-1])

#in and not in operators
print(1 in tuple)
print(2 not in tuple)
