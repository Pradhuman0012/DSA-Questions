# pair=['a','g']
# input_string="baagdcag"
# # op=5 
# count=0
# for i in range(len(input_string)):
#     if input_string[i]==pair[0]:
#         for j in range(i+1,len(input_string)):
#             if input_string[j]==pair[1]:
#                 count+=1
# print(count)
# TC = O(N^2)
# SC = O(1)

# -------------optimization-------------
# TC = O(N)
# SC = O(N)
pair=['a','g']
input_string="baagdcag"
n=len(input_string)
count=0
g_count=[0]*n
for i in range(n-1,-1,-1):
    if input_string[i]=='g':
        count+=1
    g_count[i]=count

pair_count=0
for i in range(n):
    if input_string[i]==pair[0]:
        pair_count+=g_count[i]

print(pair_count)