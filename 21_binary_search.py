# 8. Binary Search
# Problem: Implement binary search on a sorted array to find the index of a target element.
# Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4

def binary_search(nums,target):
    left,right=0,len(nums)-1

    while left<=right:
        mid=left+right//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid-1
        else:
            right= mid+1

nums = [-1, 0, 3, 5, 9, 12]
target = 9
res=binary_search(nums,target)
print(res)