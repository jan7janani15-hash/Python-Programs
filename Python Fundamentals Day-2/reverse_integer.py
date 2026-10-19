x=int(input("Enter number: "))
sign=1
if x<0:
    sign=-1
    x=-x
r=0
while x>0:
    r=r*10+x%10
    x//=10
print(r*sign)