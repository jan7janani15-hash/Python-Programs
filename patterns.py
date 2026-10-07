n=int(input("N: "))
for i in range(1,n+1):
    print("*"*i)
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print()