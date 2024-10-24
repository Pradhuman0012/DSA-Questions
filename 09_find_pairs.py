l=[1,3,5,4,7,9]
k=10
def find_pairs(l,k):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==k:
                print(l[i],l[j])

if __name__ == "__main__":
    find_pairs(l,k)


# --------------------------------------------------------------------------
# Optimization (O(n) Complexity):
# improve this by using a set to store the numbers we've already checked. This allows us to find pairs 
# in a single pass through the list, reducing the time complexity to O(n).

def find_pairs(l, k):
    seen = set()  # To store numbers we've already encountered
    for num in l:
        target = k - num
        if target in seen:  # If the counterpart is in the set, print the pair
            print(num, target)
        seen.add(num)  # Add the current number to the set

# Example usage
l = [1, 3, 5, 4, 7, 9]
k = 10
find_pairs(l, k)
