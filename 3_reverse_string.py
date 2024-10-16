# reverse_string.py
"""
2. Reverse a String
Question: Write a function that takes a string as input and returns the string reversed.

Input: "hello"
Output: "olleh"

"""

def reverse_string(s):
    # Method 1: Slicing
    method1 = s[::-1]
    
    # Method 2: Using reversed() and join
    method2 = "".join(reversed(s))
    
    # Method 3: Using a loop
    method3 = ''
    for i in range(len(s) - 1, -1, -1):
        method3 += s[i]
    
    return method1, method2, method3

# Example usage
if __name__ == "__main__":
    inp = "hello"
    result1,result2,result3 = reverse_string(inp)
    result1,result2,result3 = reverse_string(inp)
    result1,result2,result3 = reverse_string(inp)
    print("Reversed method1:", result1)
    print("Reversed method2:", result2)
    print("Reversed method3", result3)
