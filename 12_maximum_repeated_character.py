#Find the maximum_repeated_character in a string without having o(n2) complexity.
def maximum_repeated_character(s):
    result={}
    max_count_chr = ''
    max_count=0
    for chr in s:
        if chr in result.keys():
            result[chr]+=1
        else:
            result[chr]=1
        
        if result[chr]>max_count:
            max_count_chr=chr
            max_count=result[chr]



        
    return max_count_chr,max_count

s='itinnressseiiiiiiinn'
print(maximum_repeated_character(s))