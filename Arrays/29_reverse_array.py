a=[1,2,3,4,5,6,7]
i=0
j=len(a)-1

while i<=j:
    # Python uses tuple packing and unpacking to perform the swap operation
    # temp = (a[j], a[i])
    # At this point, the values of a[i] and a[j] are stored safely in the tuple, so nothing is “lost.”
    # a[i] = temp[0]
    # a[j] = temp[1]
    a[i],a[j]=a[j],a[i]
    i+=1
    j-=1
print(a)