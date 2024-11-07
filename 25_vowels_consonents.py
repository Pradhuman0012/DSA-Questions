class Solution:
    def solve(self,s):
        vowel=0
        cons=0
        for i in s:
            if i.lower() in ['a','e','i','o','u']:
                vowel+=1
            else:
                cons+=1
        return vowel,cons

solution=Solution()
inp_str='aeiou'
v,c= solution.solve(inp_str)
print(v,c)