arr = [2, 1, 3, 4, 5]
a = len(arr)
result = [1]* a
prefix = 1
for i in range(1, a):
    result[i]=prefix
    prefix*=arr[i]
suffix = 1
for i in range(a-1, -1, -1):
    result[i]*=suffix
    suffix*=arr[i]
print("Product array:", result)