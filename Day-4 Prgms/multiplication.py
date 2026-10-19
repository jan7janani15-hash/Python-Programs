n=int(input())
c=0
for i in range(1,21):
    r=n*i
    if r>100:
        break
    if r%3==0:
        c+=1
        continue
    print(n,"x",i,"=",r)
print("Skipped results:",c)