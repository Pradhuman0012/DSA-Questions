# 8. Binary Search
# Problem: Implement binary search on a sorted array to find the index of a target element.
# Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4

def binary_search(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i

nums = [-1, 0, 3, 5, 9, 12]
target = 9
res=binary_search(nums,target)
print(res)