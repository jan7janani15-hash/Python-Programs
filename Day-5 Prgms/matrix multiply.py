a=[[1,2,3],[4,5,6]]
b=[[7,8],[9,10],[11,12]]
if len(a[0])!=len(b):
    print("Invalid dimensions")
else:
    c=[]
    for i in range(len(a)):
        row=[]
        for j in range(len(b[0])):
            s=0
            for k in range(len(b)):
                s+=a[i][k]*b[k][j]
            row.append(s)
        c.append(row)
    print("Product matrix:")
    for row in c:
        print(*row)