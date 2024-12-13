arr = [2]
max_elem=float("-inf")
second_max=float("-inf")
for i in arr:
    if i>max_elem:
        second_max=max_elem
        max_elem=i

if second_max == float("-inf"):
    second_max = -1

print(second_max)

