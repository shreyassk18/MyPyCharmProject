#Approach1
mylist=[3,76,1,4,58,3,1,3,5,2]
x=int(input("Enter number to count"))
count=0

for i in mylist:
    if i==x:
        count += 1

print("{} occured {} times in a list".format(x,count))

#Approach
mylist=[3,76,1,4,58,3,1,3,5,2]
x=1

print("{} occured {} times in a list".format(x,mylist.count(x)))

