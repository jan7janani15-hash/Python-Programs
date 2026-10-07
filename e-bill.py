name=input("Customer: ")
u=int(input("Units: "))
if u<=100:
    a=u*2
elif u<=200:
    a=200+(u-100)*3
else:
    a=500+(u-200)*5
print("Customer :",name)
print("Units :",u)
print(f"Amount:₹{a:.2f}")