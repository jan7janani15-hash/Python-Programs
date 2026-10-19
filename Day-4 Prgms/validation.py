n=l=s=t=0
while True:
    a=int(input())
    if a==-1:
        break
    if a==0:
        pass
    elif a<0:
        continue
    elif a<=1000:
        n+=1
        t+=a
    elif a<=5000:
        l+=1
        t+=a
    else:
        s+=1
        t+=a
        if s==3:
            break
print("Normal transactions:",n)
print("Large transactions:",l)
print("Suspicious transactions:",s)
print("Total valid amount:",t)