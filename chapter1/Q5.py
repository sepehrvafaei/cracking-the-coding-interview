def func(s1,s2):
    l1=len(s1)
    l2=len(s2)
    count=0
    if l1==l2:
        for i in range(l1):
            if s1[i]!=s2[i]: count+=1
        if count>1:return False
        else:return True
    elif l1==l2+1:
        j=0
        for i in range(l2):
            if s2[i]!=s1[j]:
                if s2[i]!=s1[j+1]:return False
                else: j+=2
            else:j+=1
        return True
    elif l1==l2-1:
        j=0
        for i in range(l1):
            if s1[i]!=s2[j]:
                if s1[i]!=s2[j+1]:return False
                else: j+=2
            else:j+=1
        return True
    else:
        return False

print(func("pair","pabrr"))
