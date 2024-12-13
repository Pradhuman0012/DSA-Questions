arr=[1,1,2,4,7,9,5,3,7,9,9]
# output = 8
count=0
max_elem=arr[0]
for i in arr:
    if i>max_elem:
        max_elem=i
        count=1
    elif i==max_elem:
        count+=1


for i in arr:
    if max_elem==i:
        count+=1

print(len(arr)-count)