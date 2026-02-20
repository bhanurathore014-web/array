arr = [1, 2, 3, 4]
min_val = arr[0]
max_diff = arr[1]-arr[0]
for i in range(1, len(arr)):
    if arr[i] - min_val > max_diff:
        max_diff = arr[i] - min_val
    if arr[i] < min_val:
        min_val = arr[i]
print("Maximum difference between two elements in the array:", max_diff)

