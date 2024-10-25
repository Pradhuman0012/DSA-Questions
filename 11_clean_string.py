# 11_remove_puncutualtion.py
# "hi! my name@ is# luc%ky" to "hi my name is lucky"

def clean_string(s):
    res=''
    for chr in s:
        if (chr >= 'A' and chr <= "Z") or (chr>='a' and chr<='z') or chr ==' ':
            res+=chr
    return res
s="hi! my name@ is# luc%ky"
result=clean_string(s)
print(result)