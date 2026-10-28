def top_k_frequent(nums,k):
    freq={}
    for n in nums:
        freq[n]=freq.get(n,0)+1
    values=sorted(freq,key=lambda x:freq[x],reverse=True)
    return values[:k]
nums=[1,1,1,2,2,3]
k=2
print("Top",k,"frequent values:",top_k_frequent(nums,k),"(order may vary)")