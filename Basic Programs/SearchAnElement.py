#Approach1
mylist = [1,2,3,4,5]
ele=int(input("Enter number to search"))
flag=0

for i in mylist:
    if (i==ele):
        print("Element Found")
        flag=1
        break

if (flag==0):
    print("Element not found")

# #Approach2
# mylist1=[1,3,6,8,9]
# ele1=int(input("Enter number to search"))
#
# if ele1 in mylist1:
#     print("Element Found")
# else:
#     print("Not found")