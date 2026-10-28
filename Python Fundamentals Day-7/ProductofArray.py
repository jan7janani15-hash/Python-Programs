def product_except_self(nums):
    result=[]
    for i in range(len(nums)):
        p=1
        for j in range(len(nums)):
            if i!=j:
                p*=nums[j]
        result.append(p)
    return result
nums=[1,2,3,4]
print("Product array:",product_except_self(nums))