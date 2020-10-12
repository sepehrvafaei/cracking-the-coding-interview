def func(M):
    rows=len(M)
    cols=len(M)
    rowZeroHasZero=False
    colZeroHasZero=False
    #--------------------------
    for i in range(cols):
        if M[0][i]==0:
            rowZeroHasZero=True
            break
    for i in range(rows):
        if M[i][0]==0:
            colZeroHasZero=True
            break
    #--------------------------
    for i in range(1,rows):
        for j in range(1,cols):
            if M[i][j]==0:
                M[0][j]=0
                M[i][0]=0
    #--------------------------
    for i in range(cols):
        if M[0][i]==0:
            for j in range(rows):
                M[j][i]=0
    for i in range(rows):
        if M[i][0]==0:
           for j in range(cols):
               M[i][j]=0
    #--------------------------
    if rowZeroHasZero:
        for i in range(cols): M[0][i]=0
    if colZeroHasZero:
        for i in range(rows): M[i][0]=0
    return M

print(func([[1,1,1],[1,0,1],[1,1,0]]))
