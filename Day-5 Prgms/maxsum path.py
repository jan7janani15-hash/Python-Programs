r,c=map(int,input().split())
a=[]
for i in range(r):
    a.append(list(map(int,input().split())))
dp=[[0]*c for i in range(r)]
dp[0][0]=a[0][0]
for i in range(1,r):
    dp[i][0]=dp[i-1][0]+a[i][0]
for j in range(1,c):
    dp[0][j]=dp[0][j-1]+a[0][j]
for i in range(1,r):
    for j in range(1,c):
        dp[i][j]=a[i][j]+max(dp[i-1][j],dp[i][j-1])
i=r-1
j=c-1
path=[]
while i>0 and j>0:
    path.append(a[i][j])
    if dp[i-1][j]>dp[i][j-1]:
        i-=1
    else:
        j-=1
while i>0:
    path.append(a[i][0])
    i-=1
while j>0:
    path.append(a[0][j])
    j-=1
path.append(a[0][0])
path.reverse()
print("Maximum path sum:",dp[r-1][c-1])
print("Path:",path)