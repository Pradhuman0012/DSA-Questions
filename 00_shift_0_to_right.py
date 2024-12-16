arr=[12,0,0,0,0,34,0,0,0,3,4,5,2.-1,-5]
arr= [ i for i in arr if i !=0 ] + [0]* arr.count(0)
print(arr)
