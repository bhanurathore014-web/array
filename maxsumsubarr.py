# Maximum Sum Subarray (Kadane's Algorithm)

arr = [12, 15, 5, 6, 2, 25]
max_sum = 0
current_sum = 0
for num in arr:
    current_sum += num
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0
print("Maximum sum of a subarray is:", max_sum)