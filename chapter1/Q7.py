def func(matrix):
    N=len(matrix)
    if N!=len(matrix[0]):return False
    for i in range(0,int(N/2)):
        for j in range(i,N-1-i):
            temp=matrix[N-1-j][i]
            matrix[N-1-j][i]=matrix[N-1-i][N-1-j]
            matrix[N-1-i][N-1-j]=matrix[j][N-1-i]
            matrix[j][N-1-i]=matrix[i][j]
            matrix[i][j]=temp
    return matrix

print(func([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
