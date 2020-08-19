#**kwargs allows us to pass key value parameters as arguments to a function
#Here two stars represent key and a value


#Example1   Passing arguments to a function
def my_args(a,b,c):
    print(a,b,c)

a={'a':"tom", 'b':"dick", 'c':"harry"}
my_args(**a)

#Example2   Reciaving arguments to a function
def my_func(**kwargs):
    for i,j in kwargs.items():
        print(i,j)

my_func(name="John", age=21, salary=10000.00, role="Engineer")

#Example3
def my_func(**kwargs):
    for i,j in kwargs.items():
        print(i,j)

b={'name':"Shreyas", 'age':27, 'salary':20000.00, 'role':"CEO"}
my_func(**b)


