def find_even_count_in_ranges(array, ranges):
    n=len(array)
    even_prefix=[]
    evencount=0

    for i in range(n):
        if array[i]%2==0:
            evencount+=1
        even_prefix.append(evencount)

    res=[]
    for start, end in ranges:
        even_count= even_prefix[end]-(even_prefix[start-1] if start>0 else 0)
        res.append(even_count)
    return res

array = [1,2,4,3,4,8]
ranges = [[0,3],[2,5]]


res=find_even_count_in_ranges(array,ranges)
print(res)