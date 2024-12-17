arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 7, 8, 2]
]

for r in range(len(arr)):
    sum=0
    for c in range(len(arr[r])):
        sum+=arr[r][c]
    print(sum)