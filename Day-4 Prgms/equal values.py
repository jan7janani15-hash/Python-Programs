n=int(input())
a=list(map(int,input().split()))
c=1
m=1
v=a[0]
for i in range(1,n):
    if a[i]==a[i-1]:
        c+=1
    else:
        c=1
    if c>m:
        m=c
        v=a[i]
print("Value =",v)
print("Length =",m)