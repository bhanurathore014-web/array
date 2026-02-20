# Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.
arr = [4, 2, 8, 1, 3, 6, 3, 5, 2, 7]
missing_num = 2
for num in range(1, missing_num + 1):
    if num in arr:
        print(num, "is present in the array.")
    if num not in arr:
        print("Missing number: ", num)



