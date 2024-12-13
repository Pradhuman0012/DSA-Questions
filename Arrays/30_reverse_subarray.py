# Question:
# reverse a subarray of the given array from index `start` to `end`.

# Example:
# Input: arr = [10, 5, 7, 1, 9], start = 1, end = 3
# Output: [10, 1, 7, 5, 9]

def ReverseSubArray(arr,si,ei):
    while si<ei:
        arr[si],arr[ei]=arr[ei],arr[si]
        si+=1
        ei-=1
    return arr

arr = [10, 5, 7, 1, 9]
start = 1
end = 3
res=ReverseSubArray(arr,start,end)
print(res)