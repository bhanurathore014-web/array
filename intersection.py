# Find Intersection of Two Arrays: Find the common elements between two arrays.
arr1 = [1, 3, 9, 7, 4, 5]
arr2 = [2, 8, 3, 6, 7, 1]

set1 = set(arr1)
set2 = set(arr2)
intersection = list(set1 & set2)
print("Intersection:", intersection)
