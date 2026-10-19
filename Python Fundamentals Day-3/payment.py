n=int(input("Transactions: "))
a=[]
r=0
for i in range(n):
    try:
        x=float(input())
        if x<0:
            r+=1
        else:
            a.append(x)
    except:
        r+=1
if a:
    print("Successful Transactions:",len(a))
    print("Total Amount:₹%.2f"%sum(a))
    print("Highest Transaction:₹%.2f"%max(a))
    print("Lowest Transaction:₹%.2f"%min(a))
    print("Average Transaction:₹%.2f"%(sum(a)/len(a)))
print("Rejected Transactions:",r)