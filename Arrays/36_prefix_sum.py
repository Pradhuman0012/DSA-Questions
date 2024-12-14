# equilibrium endices

# a=[-3,2,4,-1]
# n=len(a)
# res=0
# for i in range(n):
#     left=sum(a[:i])
#     right=sum(a[i+1:n])
#     print(left," = ",right)
#     if left==right:
#         res +=1


# print(res)
# tc= O(n^2)
# sc= O(1)

# O(i) + O(n - i - 1) = O(n)

# This is because i + (n - i - 1) \approx n - 1, which is O(n).
# 	5.	Overall Time Complexity:
# Since the outer loop runs n times, and for each iteration the work is O(n), the total time complexity is:

# O(n) \times O(n) = O(n^2)


def equilibrium_indices_prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0] #10
    
    # Step 1: Build the prefix sum array
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    print("prefix: ",prefix)
    result = []
    
    # Step 2: Check for equilibrium index
    for i in range(n):
        # Left sum
        left_sum = prefix[i - 1] if i > 0 else 0
        # Right sum
        right_sum = prefix[n - 1] - prefix[i]
        
        if left_sum == right_sum:
            result.append(i)
    
    return result

# Example usage
a = [10, 12, 14, 18, 16]
print("given: ",a)
indices = equilibrium_indices_prefix_sum(a)
print("Equilibrium indices (prefix sum):", indices)

# tc=o(n)
# sc=o(n)