pair=['a','g']
input_string="baagdcag"
# op=5 
count=0
for i in range(len(input_string)):
    for j in range(i+1,len(input_string)):
        if input_string[i]==pair[0]:
            if input_string[j]==pair[1]:
                count+=1
print(count)
# TC = O(N^2)
# SC = O(1)