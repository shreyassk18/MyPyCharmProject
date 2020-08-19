# prim number is always greater than 1
# It has only 2 factors : 1 and itself
# The number should be divisble by only itself

while True:
    try:
        num = int(input("Enter a number to check:\n"))
    except ValueError:
        print("Number cannot be empty.. Please Enter again")
        continue    #Return to the start of the loop
    else:
        break   #Number is not empty we can come out of the loop and execute further program

count = 0
if num > 1:
    for i in range(1, num+1):
        if (num%i) == 0:  # dividing num by range in the loop
            count += 1      #Increasing number of counts if number is divisible
    if count == 2:  # If there are only 2 factors then its a prime number
        print("Number is Prime")
    else:
        print("Number is not Prime")

else:
    print("Number must be greated than one")