#Exception is an abnormal condition
#it is an event that disrupts the normal flow of the program
#In python every exception is treated as an error
#There is a difference between error and exception
    # a. An error can be syntax error or logical error
    # b. An exception is occured by user input or we can say at run time
#Exception handling keywords are: try, except, else, finally

#Example1
print("Program has started")

try:
    print(10/0) #ZeroDivisionError
    #print(10/2)    #If this executes, except block will be ignored and program will run normally
except ZeroDivisionError:
    print("Entered into except part - Handled exception")

print("Program has ended")

#if try block throws any exception. then only except block will execute, else except block is not executed

#Example2
#Defining multiple except blocks
print("Program has started")

try:
    print(10/0) #ZeroDivisionError

except TypeError:
    print("Entered into except block - Handled TypeError exception")

except ZeroDivisionError:
    print("Entered into except block - Handled ZeroDivisionError exception")

print("Program has ended")
