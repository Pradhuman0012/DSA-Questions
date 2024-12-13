def RangeSum(a,b):
    res=[]
    for i in b:
        sum=0
        for j in range(i[0],i[1]+1):
            sum+=a[j]
        res.append(sum)
    return res
        

a = [1,2,3,4,5]
b = [[0,3],[1,2]]

res=RangeSum(a,b)
print(res)