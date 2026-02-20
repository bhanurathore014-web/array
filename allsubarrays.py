# Find All Subarrays

arr = [12, 15, 5, 6, 2, 25]
subarrays = []
for i in range(len(arr)):
    for j in range(i, len(arr)):
        subarrays.append(arr[i:j+1])
print("All subarrays of the given array:", subarrays)