p=[]
while True:
    x=input()
    if x=="done":
        break
    p.append(float(x))
s=sum(p)
d=s*0.05
t=(s-d)*0.05
print("Subtotal",s)
print("Discount",d)
print("Tax",t)
print("Final",s-d+t)