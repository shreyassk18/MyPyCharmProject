#Maximum of an array
arr = [10,20,34,52,12,8]
max = arr[0]    #Assume 10 as a maximum number (zero indicates index of a number)
n = len(arr)    #Length for iteration

for i in range(1,n):
    if arr[i]>max:  #if i is greater than max, place it in index zero
        max=arr[i]

print("Maximum of array is:",max)

#Minimum of an array
arr = [10,20,34,52,12,8]
min = arr[0]    #Assume 10 as a minimum number (zero indicates index of a number)
n = len(arr)    #Length for iteration

for i in range(1,n):
    if arr[i]<max:  #if i is less than min, place it in index zero
        min=arr[i]

print("Minimum of array is:", min)