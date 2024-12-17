arr = [
    [1, 2, 3],
    [5, 6, 7],
    [9, 7, 8]
]
print("left-right diagonals:-")
i,j=0,0
n=len(arr)
while i<n and j<n:
    print(arr[i][j])
    i+=1
    j+=1
print()
print("right-left diagonals:-")

n=len(arr)
i,j=0,n-1
while i<n and j>=0:
    print(arr[i][j])
    i+=1
    j-=1

    