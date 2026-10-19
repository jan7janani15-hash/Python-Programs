n=int(input("N: "))
num=int(input("Number: "))
print("Primes:",end=" ")
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
fact=1
for i in range(1,n+1):
    fact*=i
print("\nFactorial:",fact)
a=0
b=1
print("Fibonacci:",end=" ")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
s=0
r=0
while num>0:
    d=num%10
    s+=d
    r=r*10+d
    num//=10
print("\nDigit Sum:",s)
print("Reverse:",r)