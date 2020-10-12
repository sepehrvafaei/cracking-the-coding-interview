def func(s):
    MAX_CHAR=256
    H=[0]*MAX_CHAR
    count=0
    for i in range(len(s)):
        H[ord(s[i])]+=1
    for i in range(MAX_CHAR):
        if H[i]%2==1:
            count+=1
    return count<=1
