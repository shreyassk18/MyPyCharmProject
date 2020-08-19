#Strings are immutable, which means address of the variable will be changed when you modify the variable
#memory of a variable can be found using id() funtion

str1 = "name"
str2 = "organization"

print(id(str1)) #1758994627248
print(id(str2)) #1759026452144

str2=str2 + "onmobile"

print(id(str1)) #1758994627248
print(id(str2)) #1759026457672  #so this variable address got changed as we have changed the value