a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
b=[]
for i in range(len(a)):
    if i%2==0:
        b.extend(a[i])
    else:
        b.extend(a[i][::-1])
print("Zigzag list:",b)