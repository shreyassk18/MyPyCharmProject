#Approach1
a,b=10,20
print("Numbers before swapping",a,b)

a,b=b,a
print("Numbers after swapping",a,b)

#Approach2 using temporary variable
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

print("Value of num1 before swapping",num1)
print("Value of num2 before swapping",num2)

temp=num1
num1=num2
num2=temp

print("Value of num1 after swapping",num1)
print("Value of num2 after swapping",num2)



