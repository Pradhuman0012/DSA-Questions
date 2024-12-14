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
    total=0
    for i in range(1,n):
        prefix[i]=prefix[i-1]+a[i]

    for start, end in b:
        total=prefix[end]-(prefix[start-1] if start>0 else 0)
        res.append(total)
    return res

a = [1,2,3,4,5]
b = [[0,3],[1,2]]


res=RangeSumPrefix(a,b)
print(res)
# time complexity O(n)