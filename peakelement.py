# Find Peak Element: A peak element is greater than its neighbors. Find one such element.

arr = [1, 3, 7, 3, 2, 1, 3, 2, 5]
a = len(arr)
for i in range(1, a-1):
    if (i == 0 or arr[i] > arr[i-1]) and (i == a-1 or arr[i] > arr[i+1]):
        print("Peak element:", arr[i])

