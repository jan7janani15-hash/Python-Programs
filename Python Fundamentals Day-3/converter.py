a=int(input("Number 1:"))
b=int(input("Number 2:"))
print("Binary:", format(a,'b'))
print("Octal:", format(a,'o'))
print("Hexadecimal:",format(a,'X'))
x,y=a,b
while y:
    x,y=y,x % y
print("GCD:",x)
print("LCM:",a*b//x)