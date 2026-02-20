arr = [1, 3, 9, 7, 4, 2, 5, 3, 7, 1]
target_sum = 10
subarrays = []
for i in range(len(arr)):
    current_sum = 0
    for j in range(i, len(arr)):
        current_sum += arr[j]
        if current_sum == target_sum:
            subarrays.append(arr[i:j+1])
print("Subarrays with sum", target_sum, ":", subarrays)