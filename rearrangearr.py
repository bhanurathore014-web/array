# Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.

arr = [12, 15, 5, 6, 2, 25]
arr.sort()
result = [0]
l = 0
r = len(arr) - 1
while l < r:
    result.append(arr[r])
    r -= 1
    if l < r:
        result.append(arr[l])
        l += 1
print("Rearranged array:", result)