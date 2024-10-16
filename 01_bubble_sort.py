# sorts a list of numbers in ascending order without using any built-in sorting functions.
"""
Sorts an array using the bubble sort algorithm.

Input: [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
"""

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    return nums


nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = bubble_sort(nums)
print("Sorted array:", sorted_nums)