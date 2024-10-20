# Input: 5
# Output: 5  # The sequence is 0, 1, 1, 2, 3, 5

# def fibonacci(n):
#     seq=[0,1]
#     for i in range(2,n+1):
#         fib=seq[i-1]+seq[i-2]
#         seq.append(fib)
#     return seq

# result = fibonacci(5)
# print(result)


# def fibonacci(n):
#     x,y=0,1
#     while True:
#         yield x
#         x,y = y, x+y

# n=5
# fib_gen = fibonacci(n)

# for _ in range(n+1):
#     print(next(fib_gen))

def fib3(n):
    a,b=0,1
    for _ in range(n):
        print(a, end=" ")
        a,b = b,a+b
f=fib3(5)
