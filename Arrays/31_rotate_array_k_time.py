# Question:
# reverse a subarray of the given array from index `start` to `end`.

# Example:
# Input: arr = [10, 5, 7, 1, 9], k=2
# Output: [10, 1, 7, 5, 9]

def ReverseArray(arr,si,ei):
    
    while si<ei:
        arr[si],arr[ei]=arr[ei],arr[si]
        si+=1
        ei-=1
    return arr

def RotateArray(arr,k):
    k=k%len(arr) # to handle cornaer case list index out of range if k size is grater then len of arr
    arr=ReverseArray(arr,0,len(arr)-1)
    arr=ReverseArray(arr,0,k-1)
    arr=ReverseArray(arr,k,len(arr)-1)

    return arr

arr = [10, 5, 7, 1, 9]
print(arr)
k=6
# [1,9,10,5,7]
res=RotateArray(arr,k)
print(res)