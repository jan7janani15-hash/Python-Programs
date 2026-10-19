n=int(input())
seen=[]
while n!=1 and n not in seen:
    seen.append(n)
    s=0
    for x in str(n):
        s+=int(x)**2
    n=s
print(n==1)