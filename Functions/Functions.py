#Functions are the re-usable pieces of code which helps us to organize structure of the code.
#We create functions so that we can run a set of statements multiple times during in the program without repeating.

#sample function example
def myfun():
    pass    # this will omit the body of the function. when we call this function, nothing will happen


myfun() #calling myfun function

#different ways of creating functions

#example1
def sum(start,end):
    result = 0
    for i in range(start,end+1):
        result=result+i
    print(result)

sum(10,20)

#using return in the function
def sum(start,end):
    result = 0
    for i in range(start,end+1):
        result=result+i
    return (result)

s = sum(10,20)
print(s)

#example3
def sum(start,end):
    if (start > end):
        print("Start should be less than end")
        return  #by default return function will return None (Even if we do not specify return function)
    else:
        result = 0
        for i in range(start,end+1):
            result=result+i
        return (result)

s = sum(5,1)
print(s)