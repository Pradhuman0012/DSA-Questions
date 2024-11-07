def first_occurrence(str,target):
    for i in range(len(str)):
        if ord(str[i]) == target:
            return i
    return -1

str="aabbcc"
target=98
# str="abc" 
# target=100

res=first_occurrence(str,target)
print(res)