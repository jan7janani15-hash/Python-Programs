nums=[1,1,1]
k=2
count=0
total=0
d={0:1}
for n in nums:
    total+=n
    count+=d.get(total-k,0)
    d[total]=d.get(total,0)+1
print("Count:",count)