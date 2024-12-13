arr=[1,9,2,4,5,7,3]
k=18
def CheckSum(arr,k):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]+arr[j] == k):
                print(arr[i]," + ",arr[j])
                return True
    return False
res=CheckSum(arr,k)
print(res)

