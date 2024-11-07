class Solution:
    def solve(self, A):
        res = ''
        for i in A:
            res += i.upper() if i.islower() else i
        return res


solution = Solution()
input_string = "hello World"
result = solution.solve(input_string)
print(result)  