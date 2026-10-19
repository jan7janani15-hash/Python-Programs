a=int(input("a="),2)
b=int(input("b="),2)
s=a+b
r=""
while s>0:
    r=str(s%2)+r
    s//= 2
print(r or "0")