s='scaler'
op='s19c3a1l12e5r18'
alph= [chr(i) for i in range(97,123)]
num=[i for i in range(1,27)]
res=dict(zip(alph,num))
final_str=''
for i in s:
    final_str+=i+str(res[i])
print(final_str)



# s = 'scaler'
# op = ''.join([char + str(ord(char) - 96) for char in s])  # ord(char) - 96 to get a=1, b=2, etc.
# print(op)