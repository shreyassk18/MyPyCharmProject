#Global varible - it is defined outside of the function and can be accessed within or outside of the function
#local variable - It is defined inside a function and can be accessed only within a function

#example1
global_var = 100    #global varianle

def myfun():
    local_var = 50  #local variable
    print(global_var)   #we can access global variable inside a function

myfun()

#print(local_var)    #NameError: name 'local_var' is not defined, as local variable cannot be accessed outside of the function
print(global_var)

#example2 using same name for global and local variable
x = 100

def fun():
    x = 200
    print(x)    #this wl print x as 200

fun()
print(x)    #this will print global variable

#making local variable as global
a = 10

def change():
    #a=20
    global a    #change local to global
    a=100000
    print(a)

change()
