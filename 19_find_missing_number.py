'''Find Missing Number
Problem: Given an array of size n-1 with elements from 1 to n, find the missing number.
Input: [1, 2, 4, 5] (for n = 5)
Output: 3'''
arr=[4, 2, 3, 5]
n=5


# ------------------------------------------------------------------------------------------------------
# hashmap  approch 
# TC = o(n)
# SC = o(n)
def find_missing_number(nums, n):
    hash_map={i:False for i in range(1,n+1)} # Step 1: Create a hash map (dictionary) to track numbers
    for i in nums:
        if i in hash_map:
            hash_map[i]=True # Step 2: Mark each number in the array as present in the map

    for i in range(1,n+1):
        if not hash_map[i]: # Step 3: Find the missing number by checking the map
            return i

missing_number = find_missing_number(arr, n)
print("Missing number:", missing_number)

# ------------------------------------------------------------------------------------------------------
# sum formula approch 
# TC = o(n)
# SC = o(1) integer overflow error may occur

def find_missing_number(nums, n):
    sa=0
    sn=n*(n+1)//2 #sum of n natural numbers
    for i in nums:
        sa+=i # sum of array
    return sn-sa

# missing_number = find_missing_number(arr, n)
# print("Missing number:", missing_number)

# ------------------------------------------------------------------------------------------------------
# xor approch (optimal solution)
# TC = o(n)
# SC = o(1)

def find_missing_number(nums, n):
    # Step 1: XOR all numbers from 1 to n
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i
    
    # Step 2: XOR all elements in the array
    xor_array = 0
    for num in nums:
        xor_array ^= num
    
    # Step 3: XOR the results to get the missing number
    missing_number = xor_all ^ xor_array
    return missing_number



# missing_number = find_missing_number(arr, n)
# print("Missing number:", missing_number)



