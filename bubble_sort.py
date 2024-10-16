# sorts a list of numbers in ascending order without using any built-in sorting functions.

def bubble_sort(nums):
    """
    Sorts an array using the bubble sort algorithm.
    
    Parameters:
    nums (list): A list of numbers to be sorted.
    
    Returns:
    list: The sorted list.
    """
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    print(nums)


nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = bubble_sort(nums)
print("Sorted array:", sorted_nums)