'''a=input("Enter first number:")  #10
b=input("Enter second number:") #20

print(a+b)  # output will be 1020   #By default entered value type will be string
########################################

a=int(input("Enter first number:"))  #10
b=int(input("Enter second number:")) #20

print(a+b)  #output will be 30
########################################

a=input("Enter first number:")  #10
b=input("Enter second number:") #20

print(int(a)+int(b))  # output will be 30
########################################

a=input("Enter first decimal number:")  #3.5
b=input("Enter second decimal number:") #3.6

print(float(a)+int(b))  #ValueError: invalid literal for int() with base 10: '3.6'

'''
a=list(input("Enter a list of numbers:"))
print(a)
