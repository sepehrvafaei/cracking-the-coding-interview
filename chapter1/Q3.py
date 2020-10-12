def func(s,l):
    L=len(s)
    j=0
    sp=[0]*L
    for i in range(l):
        if s[i]==' ':
            sp[j]='%'
            sp[j+1]='2'
            sp[j+2]='0'
            j+=3
        else:
            sp[j]=s[i]
            j+=1
    return "".join(sp)
        
