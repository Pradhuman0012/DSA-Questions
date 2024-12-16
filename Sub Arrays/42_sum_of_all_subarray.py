arr = [1,2,3,4]
res = []

for i in range(len(arr)):
    sum=0
    for j in range(i, len(arr)):
        sum+=arr[j]
        res.append(sum)
    print()
        
print(res)