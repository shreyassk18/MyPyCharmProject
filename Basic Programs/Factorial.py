#We need to multiply all the numbers, coming before a specified number 'num' along with num
#if num =5, factorial = 1*2*3*4*5
#Number must be greater than zero

#Iterative Approach

# factorial=1
# num=int(input("Enter a number\n"))
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("Factorial of 0 is 1")
# else:
#     for i in range(1, num+1):
#         factorial = factorial * i
#     print("Factorial of %d is %d"%(num,factorial))

#Recursive Approach
# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)
#
# n = int(input("Enter a number\n"))
# print("Factorial of %d is %d"%(n,fact(n)))


#Ternary Approach
def factorial(num):
    return 1 if (num==0 or num==1) else num * factorial(num-1)

num = int(input("Enter a number\n"))
print("Factorial of %d is %d"%(num,factorial(num)))



