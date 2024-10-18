# 5. Find the First Unique Character in a String
# Problem Statement:

# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
# Input: s = "leetcode"
# Output: 0

# Input: s = "loveleetcode"
# Output: 2


def find_unique_index(s):
    exist={}
    for i in range(len(s)):
        if s[i] in exist.keys():
            exist[s[i]]+=1
        else:
            exist[s[i]]=1

    for i in range(len(s)):
        if exist[s[i]] < 2:
            return i
    return -1


s = "loveleetcode"
res= find_unique_index(s)
print(res)