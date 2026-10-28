def find_max_length(nums):
    balance=0
    seen={0:-1}
    longest=0
    for i in range(len(nums)):
        if nums[i]==0:
            balance-=1
        else:
            balance+=1
        if balance in seen:
            longest=max(longest,i-seen[balance])
        else:
            seen[balance]=i
    return longest
nums=[0,1,0]
print("Maximum balanced subarray length:",find_max_length(nums))