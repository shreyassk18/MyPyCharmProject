#differnet ways of passing arguments

#arguments with default values(positional)

def add (i,j=100):  #default value for j will be 100, we dont need to pass the j value in calling function
    print(i+j)

add(50)

#or
def sum(a,b=100):
    print(a+b)

sum(50,250)

#keyword arguments
def named_args(name,greeting):
    print(greeting + "",name)

named_args("shreyas", "hi") #POSITIONAL ARGUMENT

named_args(name="abhishek", greeting="Hello")       #KEYWORD ARGUMENT
named_args(greeting="good morning", name="Kiran")   #KEYWORD ARGUMENT

#Combination of positional and keyword arguments
def myFun(a,b,c):
    print(a,b,c)

myFun(10,20,30)         #POSITIONAL ARGUMENT
myFun(10,b=40,c=80)     #First POSITIONAL and 2ND 3RD KEYWORD ARGUMENT
myFun(1,100,c=400)    #First POSITIONAL and 2ND 3RD KEYWORD ARGUMENT

#myFun(1,100,b=400)  #TypeError: myFun() got multiple values for argument 'b'    #position matters here

#myFun(3,b=20,13)  #SyntaxError: positional argument follows keyword argument
                  #This is not allowed in python, first we have to specify all positional arguments and then we have to specify keyword arguments
