# Rotate Array to the Left by k Positions

arr = [1,2,3,4,5,6,7,8,9,10]
k  = 3
arr = arr[::1]
arr = arr[k:] + arr[:k]
print(arr)