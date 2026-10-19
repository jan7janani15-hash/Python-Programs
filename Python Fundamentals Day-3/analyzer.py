a = int(input("Start: "))
b = int(input("End: "))
for n in range(a,b+1):
    p=n>1
    for i in range(2,n):
        if n % i==0:
            p=False
            break
    s = sum(int(x) 
            for x in str(n))
    perfect = sum(i for i in range(1,n) 
                  if n%i==0)==n
    arm = sum(int(x)**len(str(n))
              for x in str(n))==n
    pal = str(n) == str(n)[::-1]
    print(n,p,perfect,arm,pal,s,len(str(n)),bin(n)[2:])