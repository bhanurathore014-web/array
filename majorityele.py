# Find Majority Element: Find the element that appears more than n/2 times.

arr = [1, 3, 7, 3, 2, 1, 3, 3, 4, 3, 5]
majority = None
count = 0

for num in arr:
    if count == 0:
        majority = num
    if num == majority:
        count += 1
    else:
        count -= 1
print("Majority Element:", majority)