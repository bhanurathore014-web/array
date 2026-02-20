# Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.

arr = [7, 2, 3, 4, 5, 6, 1]
target = 7
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Pair found: ", arr[i], arr[j])   

