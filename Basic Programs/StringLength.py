#Using for loop
str="welcome"
counter=0
for i in str:
    counter += 1

print(counter)

#Using while loop and slicing
str="welcome"
counter=0
while str[counter:]:
    counter += 1

print(counter)

#Using len method
str="welcome"
print(len(str))

#Using join and count
str="welcome to python"
randstr=","

print(randstr.join(str))    #wXeXlXcXoXmXe (Adding X at each character of str)
print(randstr.join(str).count(randstr)+1)