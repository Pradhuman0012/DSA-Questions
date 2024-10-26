# dict compression
def dict_compression(a,b):
    my_dict= {a:b for a,b in zip(a,b)}
    return my_dict

a=[1,2,3,4,5]
b=['a','b','c','d','e']
result=dict_compression(a,b)
print(result)