def is_anagram(s,t):
    if sorted(s)==sorted(t):
        print(True)
    else:
        print(False)

s = "listen"
t = "silent"
is_anagram(s,t)
