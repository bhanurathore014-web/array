# Find the First Missing Positive: Find the smallest positive integer missing in the array.

arr = [1, -5, 6, 8, 3, -2, 4, -1]
a = len(arr)
for i in range(a):
    while 1<= arr[i]<=a and arr[arr[i]-1] !=arr[i]:
        arr[i], arr[arr[i]-1]= arr[arr[i]-1], arr[i]
for i in range(a):
    if arr[i]!= i+1:
        print("First missing positive integer:", i+1)
        break
else:
    print("First missing positive integer:", a+1)























































