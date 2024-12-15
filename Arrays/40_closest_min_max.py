'''
Closest min max
explanation: Given an array find the length of the smallest subarray
which contains both min max of the array

ind   0 1 2 3 4 5 6 7 8 9 
Ex -[ 1 2 3 1 3 4 6 4 6 3 ]
ans [3-6] => [1 3 4 6] length = 4

'''
# TC = O(N^2)
# SC = O(1)

# def closest_min_max(arr):
#     n=len(arr)
#     mx=arr[0]
#     mn=arr[0]
#     for num in arr:
#         mx= num if num>mx else mx
#         mn= num if num<mn else mn
#     res=n

#     for i in range(n):
#         if arr[i]==mn:
#             for j in range(n):
#                 if arr[j]==mx:
#                     l= (j-i)+1 if j>i else (i-j)+1
#                     if l<res:
#                         res=l
#     return res

# -------------------------------
# opptimal -
# TC = O(N)
# SC = O(1)

def closest_min_max(arr):
    n=len(arr)
    mx=arr[0]
    mn=arr[0]
    min_index=-1
    max_index=-1

    for num in arr:
        mx= num if num>mx else mx
        mn= num if num<mn else mn
    ans=n


    for i in range(n-1,-1,-1):
        if arr[i]==mn:
            min_index=i
            if max_index != -1:
                res=(max_index-min_index)+1
                if res<ans:
                    ans=res

        if arr[i]==mx:
            max_index=i
            if min_index != -1:
                res=(min_index-max_index)+1
                if res<ans:
                    ans=res
    return ans

arr=[1,2,3,1,3,4,6,4,6,3]
# arr=[2,2,6,4,5,1,5,2,6,4,1]

res= closest_min_max(arr)
print(res) #4