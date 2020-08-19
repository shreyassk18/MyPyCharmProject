#The find() method finds the first occurance of a specified value
#find() method returns -1 if string not found

str="Welcome to python programming"
sub_str="python"

check=str.find(sub_str)
if (check==-1):
    print("Substring not present in a string")
else:
    print("String present at position {}".format(check))

