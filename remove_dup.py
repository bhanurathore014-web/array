arr = [1, 2, 2, 3, 4, 3, 5]
unique_arr = []
for val in arr:
    if val not in unique_arr:
        unique_arr.append(val)
print(unique_arr)