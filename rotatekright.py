# Rotate Array by k Positions: Rotate the array to the right by k positions.

arr = [1,2,3,4,5,6,7,8,9,10]
k  = 3
arr = arr[::-1]
arr = arr[:k][::-1] + arr[k:][::-1]
print(arr)

