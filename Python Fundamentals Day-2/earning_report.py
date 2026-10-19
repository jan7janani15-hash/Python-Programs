n=int(input("Number of Deliveries: "))
total=0
earn=0

for i in range(n):
    d=float(input("Distance: "))
    total+=d
    if d<=5:
        earn+=40
    else:
        earn+=40+(d-5)*8

print(f"Total Distance : {total:.2f} km")
print(f"Total Earnings : ₹{earn:.2f}")
print(f"Average Distance : {total/n:.2f} km")