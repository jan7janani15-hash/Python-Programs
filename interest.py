principal=float(input("Principal: "))
rate=float(input("Rate: "))
time=float(input("Time: "))
if principal<0 or time<0:
    print("Principal and time must be non-negative.")
else:
    si=principal*rate*time/100
    total=principal+si
    print(f"Principal:{principal:.2f}")
    print(f"Rate:{rate:.2f}%")
    print(f"Time:{time:.2f} years")
    print(f"Simple Interest:{si:.2f}")
    print(f"Total Amount:{total:.2f}")