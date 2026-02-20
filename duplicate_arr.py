#Find Duplicates in an Array
arr = [3,7,2,3,4,5,7,1,2]
seen = set()
duplicates = set()  
for val in arr:
    if val in seen:
        duplicates.add(val)
    else:
        seen.add(val)
print("Duplicate elements:", duplicates)