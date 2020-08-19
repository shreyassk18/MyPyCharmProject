#A series of numbers in which each number is the sum of the two preceding numbers
f1=0
f2=1
f = int(input("Enter a range\n"))

print("The fibonacci series for %d is:"%(f))

print(f1)
print(f2)

for i in range(1, f+1):
    fib = f1+f2
    print(fib)

    f1=f2
    f2=fib
