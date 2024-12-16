s = ['a', 'b', 'c']
res = []

for i in range(len(s)):
    for j in range(i, len(s)):
        subarray = s[i:j+1]
        res.append(subarray)  
        
print(res)