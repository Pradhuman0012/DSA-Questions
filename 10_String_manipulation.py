# String_manipulation. 
# "The Sky is Blue" to "Blue is Sky The"

def String_manipulation(s):
    res = s.split()
    return res[::-1]

result = String_manipulation("The Sky is Blue")
print(" ".join(result))