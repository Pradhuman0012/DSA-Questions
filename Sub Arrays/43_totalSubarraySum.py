def totalSubarraySum0(arr):
    total=0
    n=len(arr)
    for i in range(n):
        sum=0
        for j in range(i, n):
            sum+=arr[j]
            total+=sum
    return total
# tc = O(N^2)
# sc = O(1)




# -------optimal approch-----
def totalSubarraySum(arr):
    sum=0
    n=len(arr)
    for i in range(n):
        sum+=arr[i] * ((i+1)*(n-i))
    return sum
arr=[1,2,3,4]
res=totalSubarraySum0(arr)
print(res)
# tc = O(N)
# sc = O(1)