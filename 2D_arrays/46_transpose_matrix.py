arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def transpose(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
transpose(arr)

for i in arr:
    print(i)