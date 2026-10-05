<<<<<<< HEAD
nums=[2,7,11,15]
target=9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print([i,j])
=======
num=int(input("Enter N:"))
i=1
sum=0
while i<=num:
    sum=sum+i
    i=i+1
print("Sum=",sum)
print("Average=",sum/num)
>>>>>>> 22eb623399f34fb51b2980dd3ff7c81f23f10b0a
