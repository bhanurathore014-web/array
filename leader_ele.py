arr = [16, 13, 14, 3, 5, 12, 7, 10, 9]
leaders = []
max_from_right = arr[-1]
leaders.append(max_from_right)
for i in range(len(arr)-2, -1, -1):
    if arr[i] > max_from_right:
        max_from_right = arr[i]
        leaders.append(max_from_right)
leaders.reverse()
print("Leader elements in the array:", leaders)