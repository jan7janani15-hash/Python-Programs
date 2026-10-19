x=int(input("Enter number: "))
if x<0:
    print(False)
else:
    n=x
    r=0
    while x>0:
        r=r*10+x%10
        x//=10
    print(n==r)