def CountOccurance(a,b):
    count=0
    for i in a:
        if i==b:
            count+=1
    return count

a = [10, 5, 5, 5, 7, 1, 9]
b = 5

res=CountOccurance(a,b)
print(res)