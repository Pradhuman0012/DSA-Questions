# Input: 5
# Output: 5  # The sequence is 0, 1, 1, 2, 3, 5

def fibonacci(n):
    seq=[0,1]
    for i in range(2,n+1):
        fib=seq[i-1]+seq[i-2]
        seq.append(fib)
    return seq

result = fibonacci(5)
print(result)