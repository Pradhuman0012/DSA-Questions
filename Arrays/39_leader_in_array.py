'''
An ele is a leader if it is greater than allelements on its right
arr[N-1] is always a leader
'''

# bruteforce - 
# TC = O(N^2)
# SC = O(1)
def leader_in_array0(arr):
    count=1
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                flag=True
                
            if arr[j]>arr[i]:
                flag=False
                break
        if flag:
            count+=1
    return count
# -------------------------------
# opptimal -
# TC = O(N)
# SC = O(1)
def leader_in_array(arr):
    count=1
    n=len(arr)
    max_element=arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i]>max_element:
            max_element=arr[i]
            count+=1
    return count

# arr=[15,-1,7,2,5,4,2,3]
arr=[10,7,9,11,2,4]
res= leader_in_array(arr)
print(res) #5
