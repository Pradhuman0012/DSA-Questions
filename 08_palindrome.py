

def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):  # Only need to check up to the middle
        if s[i] != s[n - i - 1]:  # Compare characters from start and end
            return False
    return True

# def is_palindrome(s):
#     if s==s[::-1]:
#         return True
#     return False 

# Test
s = 'pradhuman'
if is_palindrome(s):
    print('Yes')
else:
    print('No')
