l,r=map(int,input().split())
found=False
for i in range(1,r+1):
    if i*i>=l and i*i<=r:
        print("First perfect square:",i*i)
        found=True
        break
if not found:
    print("No perfect square found")