# def RangeSum(a,b):
#     res=[]
#     for i in b:
#         sum=0
#         for j in range(i[0],i[1]+1):
#             sum+=a[j]
#         res.append(sum)
#     return res
        

# a = [1,2,3,4,5]
# b = [[0,3],[1,2]]

# res=RangeSum(a,b)
# print(res)

# tc=o(n^2)


# ------optimize solution using prefix-------
def RangeSumPrefix(a,b):
    prefix=[0]*len(a)
    prefix[0]=a[0]
    n=len(a)
    res=[]
    temptotal=0
    for i in range(1,n):
        prefix[i]=prefix[i-1]+a[i]

    for i in b:
        temptotal=prefix[i[1]] if i[0]<=0 else prefix[i[1]]-prefix[i[0]-1]
        res.append(temptotal)
    return res

a = [1,2,3,4,5]
b = [[0,3],[1,2]]


res=RangeSumPrefix(a,b)
print(res)