#Stements under else block will run only when no execption is raised
#Statements under finally block will run everytime no matter exception occurs or not


print("Program has started")

try:
    print(10/0) #ZeroDivisionError

except ZeroDivisionError:
    print("Entered into except block - Handled ZeroDivision exception")

except SyntaxError:
    print("Entered into except block - Handled SyntaxError exception")

else:
    print("Entered into else block...")

finally:
    print("Entered into finally block....")


print("Program has ended")



#Case1: Exception occured --> except and finally block will execute
#Case2: Exception occured but not handled--> Finally block will execute
#Case3: Exception not occured --> else and finally block will execute