a=[[0,0,5,0],[0,8,0,0],[3,0,0,6]]
b=[]
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]!=0:
            b.append((i,j,a[i][j]))
print(b)