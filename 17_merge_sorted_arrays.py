def merge_sorted_arrays(arr1, arr2):
    # Implement your logic here
    # return sorted(arr1+arr2)
    res=[]
    for i in arr1:
        for j in arr2:
            if j<i:
                res[j,i]
    return res


# Direct input
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
result = merge_sorted_arrays(arr1, arr2)
print(result)  # Expected output: [1, 2, 3, 4, 5, 6]
