a=[1,2,3,4,2,4]
# print(list(set(a)))
res=[]
duplicate=[]
for i in a:
    if i in res:
        duplicate.append(i)
    else:
        res.append(i)
print(res)
print(duplicate)