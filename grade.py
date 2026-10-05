a=float(input("Enter mark 1:"))
b=float(input("Enter mark 2:"))
c=float(input("Enter mark 3:"))
average=(a+b+c)/3
print("Average=",average)
if average>=90:
    print("Grade A+")
elif average>=75:
    print("Grade A")
elif average>=50:
    print("Grade B")
else:
    print("Fail")
