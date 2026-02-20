arr = [5, 0, 3, 0, 1, 0, 4, 7, 9, 1, 4]
non_zero= 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[non_zero] = arr[i]
        non_zero += 1
for i in range(non_zero, len(arr)):
    arr[i] = 0
print("Array after moving zeros to the end:", arr)