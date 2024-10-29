def frequency_count(s):
    clean_str=''
    for chr in s:
        if (chr >= 'A' and chr <= "Z") or (chr>='a' and chr<='z') or chr ==' ':
            clean_str+=chr
    
    s=clean_str.split()
    res={}


    for i in s:
        # print(i)
        if str(i) in res:
            res[i]+=1
        else:
            res[i]=1
    return res


res = frequency_count("hy there, there is a gir who is saying hy")
print(res)