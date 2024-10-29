# Brute Force Solution:

# Iterate over the array
# Create a nested loop
# Calculate the sum of the subarray
# Check if the sum matches the target
# If no match is found return -1


# Time Complexity = O(n^2) - Nested loops make it quadratic.
# Space Complexity = O(1) - Constant extra space is used.


def subarray_with_given_sum(arr, target_sum):
    # Implement your logic here
    for i in range(len(arr)):
        cur_sum=0
        for j in range(i,len(arr)):         
            cur_sum+=arr[j]  
            if cur_sum == target_sum:
                return [i,j]
    return -1



# input
arr = [1, 2, 3, 7, 5]
target_sum = 12
result = subarray_with_given_sum(arr, target_sum)
print(result)  # Expected output: [1, 3]


