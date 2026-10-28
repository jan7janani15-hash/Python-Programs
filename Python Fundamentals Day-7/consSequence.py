def longest_consecutive(nums):
    s=set(nums)
    longest=0
    for n in s:
        if n-1 not in s:
            count=1
            while n+count in s:
                count+=1
            longest=max(longest,count)
    return longest
nums=[100,4,200,1,3,2]
print("Longest consecutive sequence length:",longest_consecutive(nums))
print("Sequence: 1, 2, 3, 4")