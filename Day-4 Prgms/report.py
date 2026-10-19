n=int(input())
a=list(map(int,input().split()))
p=neg=z=e=o=b=c=d=f=0
for i in a:
    if i>0:
        p+=1
    elif i<0:
        neg+=1
    else:
        z+=1
    if i%2==0:
        e+=1
    else:
        o+=1
    if i!=0:
        if i%3==0 and i%5==0:
            b+=1
        elif i%3==0:
            c+=1
        elif i%5==0:
            d+=1
        else:
            f+=1
    else:
        f+=1
print("Positive:",p)
print("Negative:",neg)
print("Zero:",z)
print("Even:",e)
print("Odd:",o)
print("Divisible by both 3 and 5:",b)
print("Divisible only by 3:",c)
print("Divisible only by 5:",d)
print("Divisible by neither:",f)