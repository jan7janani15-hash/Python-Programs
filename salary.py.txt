basic=float(input("Enter basic salary:"))
hra=basic*0.20
da=basic*0.15
pf=basic*0.08
net=basic+hra+da-pf
print("HRA:",hra)
print("DA:",da)
print("PF:",pf)
print("NetSalary:",net)
