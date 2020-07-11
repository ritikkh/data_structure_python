# Defining the list
arr = [10, 20, 300, 30, 7]
#update the list
arr[1] = 22
#iterate through array
for i in arr:
    print(i)
#print list with conditions
print(arr[:-1])
#find minimum and maximum
max = arr[0]
for i in arr:
    if max < i:
        max = i
print(max)