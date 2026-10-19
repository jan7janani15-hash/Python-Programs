n=int(input("N:"))
a=int(input("Divisor 1:"))
w=input("Word 1:")
b=int(input("Divisor 2:"))
v=input("Word 2:")
for i in range(1,n+1):
    if i%a==0 and i%b==0:
        print(w+v)
    elif i%a==0:
        print(w)
    elif i%b==0:
        print(v)
    else:
        print(i)