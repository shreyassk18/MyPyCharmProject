#Check if string and reverse of a string is same

s=input("Enter a string")
print(s[:]) #Colon will print complete string
#print(s[0:5:1]) #here 0 starting index, 5 end index and 1 is steps, (increase step by 1)

rev=s[::-1] #this will give reverse of a string

if s==rev:
    print("String is palindrome")
else:
    print("String is not palindrome")
    