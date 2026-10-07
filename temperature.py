c=float(input("Enter Celsius: "))
f=(c*9/5)+32
k=c+273.15
print("Celsius:",format(c,".2f"))
print("Fahrenheit:",format(f,".2f"))
print("Kelvin:",format(k,".2f"))
print("\nConversion Table")
print("Celsius Fahrenheit  Kelvin")
for c in range(-40,101,10):
    f=(c*9/5)+32
    k=c+273.15
    print(c,"",format(f,".2f"),"",format(k,".2f"))