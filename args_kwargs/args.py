#*args allows us to pass n number of arguments to a function

#Example1
def sum(*args):
    s=0
    for i in args:
        s+=i

    print("Sum is:", s)

sum(1,2,3,4)
sum(10,20,30)


#Example2
def my_args(a,b,c,d):
    print(a,b,c,d)

args=[1,2,3,4,5]  #List
my_args(*args)  #Passing list values as parameter for a function


