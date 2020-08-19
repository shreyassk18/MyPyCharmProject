#We can return multiple values from a function using return statement by seperating them with a comma(,).
#multiple values are returns as tuples.

def bigger(a,b):
    if (a<b):
        return a,b
    else:
        return b,a

s=bigger(10,20)
print(s)
print(type(s))

