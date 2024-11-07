# chr='abfg12345'
# ch=[]
# dig=[]
# for i in chr:
#     if ord(i) in range(97,123):
#         ch.append(i)
#     else:
#         dig.append(i)
# res=len(ch) if len(ch)>len(dig) else len(dig)
# print(res)
# --------------------
def most_occur_char(chr):
    ch = sum(1 for i in chr if i.isalpha())  # Count of alphabetic characters
    dig = len(chr) - ch  # Total length minus alphabetic count gives digit count
    return max(ch, dig)

chr = 'abfg12345'
res=most_occur_char(chr)

print(res)