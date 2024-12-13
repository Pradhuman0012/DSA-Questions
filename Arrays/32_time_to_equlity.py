arr=[2,4,1,3,2]
res=0
max_elem=arr[0]
for i in range(len(arr)):
    if i>max_elem:
        max_elem=i
for i in arr:
    res+=max_elem-i
print(res)