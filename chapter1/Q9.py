def func(s1,s2):
    l1=len(s1)
    l2=len(s2)
    if l1==l2 or l1==0 or l2==0 :return False
    return (s2 in s1+s1)

print(func('abcd','cda'))
    