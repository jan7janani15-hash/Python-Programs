age=int(input("Enter age:"))
voting="Eligible"if age>=18 else "Not Eligible"
discount="Discount" if age>=60 else "No Discount"
print(voting)
print(discount)
