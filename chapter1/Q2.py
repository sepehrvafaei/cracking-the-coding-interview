#method 1

def func(x,y):
    return sorted(x)==sorted(y)

#method 2

def func(x,y):
    CHARS=256
    arr_x=[0]*CHARS
    arr_y=[0]*CHARS
    for i in range(len(x)):
        arr_x[ord(x[i])]+=1
    for i in range(len(y)):
        arr_y[ord(y[i])]+=1
    for i in range(CHARS):
        if arr_x[i]!=arr_y[i]:
            return False
    return True
