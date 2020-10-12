def func(s):
    i=0
    c_s=[]
    L=len(s)
    while i<L:
        count=1
        c_s.append(s[i])
        while  i+1<L and s[i]==s[i+1]:
            i+=1
            count+=1
        c_s.append(str(count))
        i+=1
    c_s=''.join(c_s)
    if len(c_s)<len(s):
        return c_s
    return s

print(func("aaabbbcccdaa"))