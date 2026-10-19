a=input("Entry Time: ")
b=input("Exit Time: ")
h1,m1=map(int,a.split(":"))
h2,m2=map(int,b.split(":"))
start=h1*60+m1
end=h2*60+m2
if end<start:
    end+=1440
t=end-start
h=t//60
m=t%60
bill=h
if m>0:
    bill+=1
fee=30
if bill>1:
    fee+=20*(bill-1)
print("Parking Duration:",h,"hours",m,"minutes")
print("Billable Hours:",bill)
print("Parking Fee:₹",fee)