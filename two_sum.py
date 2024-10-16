"""
2. Two Sum Problem
Finds all pairs of indices in 'nums' where the sum equals 'target'.

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]  # Because nums[0] + nums[1] = 2 + 7 = 9

"""


def two_sum(nums, target):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                res.append([i, j])
    return res


if __name__ == "__main__":
    nums = [2, 7, 5, 4]
    target = 9
    result = two_sum(nums, target)
    print("Output:", result)