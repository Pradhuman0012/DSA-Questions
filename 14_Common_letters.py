def common_letters(a,b):
    a=set(a)
    b=set(b)
    return list(a & b)

a='abcd'
b='cder'
res=common_letters(a,b)
print(res)